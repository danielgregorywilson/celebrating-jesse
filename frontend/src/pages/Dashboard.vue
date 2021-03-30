<template>
  <q-page class="q-pa-md" id="page">
    <q-spinner-cube
      size="5.5em"
      class="cube-spinner"
      v-if="showSpinner"
    />
    <div class="row q-gutter-md justify-left">
      <div v-for="memory in memories" :key="memory.key" class="memory-container row items-center justify-center" @click="openCarousel(memory.key)">
        <img v-if="memory.type == 'image'" class="memory-grid-image" :src="memory.image" />
        <div v-if="memory.type == 'story'">
          <q-icon name="auto_stories" class="memory-container-text row" size="56px"/>
          <span v-if="memory.title" class="memory-container-text row">{{ memory.title }}</span>
          <span class="memory-container-text row">Uploaded by {{ memory.uploaded_by_name }}</span>
        </div>
        <div v-if="memory.type == 'video'">
          <q-icon name="ondemand_video" class="memory-container-text row" size="56px"/>
          <span v-if="memory.title" class="memory-container-text row">{{ memory.title }}</span>
          <span class="memory-container-text row">Uploaded by {{ memory.uploaded_by_name }}</span>
        </div>
        <div v-if="memory.type == 'audio'">
          <q-icon name="headset" class="memory-container-text row" size="56px"/>
          <span v-if="memory.title" class="memory-container-text row">{{ memory.title }}</span>
          <span class="memory-container-text row">Uploaded by {{ memory.uploaded_by_name }}</span>
        </div>
      </div>
    </div>

    <q-dialog v-model="carousel" full-width full-height>
      <q-carousel
        v-model="slide"
        animated
        transition-prev="slide-right"
        transition-next="slide-left"
        swipeable
        control-color="primary"
        class="bg-gradientEnd shadow-1 rounded-borders"
        id="memory-carousel"
        :autoplay="carouselAutoplay"
        ref="carousel"
      >
        <template v-slot:control>
          <q-carousel-control
            position="top-right"
            :offset="[18, 18]"
            class="text-white rounded-borders"
            style="background: rgba(0, 0, 0, .3); padding: 4px 8px;"
          >
            <q-toggle dense dark color="primary" v-model="carouselAutoplay" label="Autoplay" />
          </q-carousel-control>

          <q-carousel-control
            position="bottom-right"
            :offset="[18, 18]"
            class="q-gutter-xs"
          >
            <q-btn
              push round dense color="primary" text-color="black" icon="arrow_left"
              @click="$refs.carousel.previous()"
            />
            <q-btn
              push round dense color="primary" text-color="black" icon="arrow_right"
              @click="$refs.carousel.next()"
            />
          </q-carousel-control>
        </template>
        <q-carousel-slide v-for="memory in memories" :key="memory.key" :name="memory.key" class="column no-wrap flex-center">
          <img v-if="memory.type == 'image'" :src="memory.image" class="memory-lightbox-image" />
          <div v-if="memory.type == 'story'" class="column flex-center">
            <q-card class="lightbox-story">
              <q-card-section>
                {{ memory.story }}
              </q-card-section>
            </q-card>
          </div>
          <video v-if="memory.type == 'video'" width="320" height="240" controls>
            <source :src="memory.video" type="video/mp4">
          </video>
          <audio v-if="memory.type == 'audio'" controls :src="memory.audio" />
          <q-card class="lightbox-metadata">
            <q-card-section>
              <span v-if="memory.title" class="row">{{ memory.title }}</span>
              <span v-if="memory.description" class="row">{{ memory.description }}</span>
              <span v-if="memory.date" class="row">Date: {{ memory.date }}</span>
              <span v-if="memory.age && memory.age != -1" class="row">Age: {{ memory.age }}</span>
              <span class="row">Uploaded by {{ memory.uploaded_by_name }} on {{ readableDate(memory.uploaded_at) }}</span>
            </q-card-section>
          </q-card>
        </q-carousel-slide>
      </q-carousel>
    </q-dialog>
  </q-page>
</template>

<style scoped lang="scss">
  #page {
    background: $darkest;
    background: linear-gradient(0deg, $gradientEnd 0%, $gradientStart 50%, );
  }
  .cube-spinner {
    position: fixed;
    top: 50%;
    left: 50%;
    margin-top: -38.5px;
    margin-left: -38.5px;
    color: $darker;
  }
  .memory-container {
    width: 250px;
    height: 250px;
    background-color: $darker;
    border-radius: 5px;
  }
  .memory-container-text {
    color: $gradientEnd !important;
  }
  .memory-grid-image {
    width: 250px;
    height: 250px;
    object-fit: cover;
    border-radius: 5px;
  }
  #memory-carousel {
    background-color: $gradientEnd;
  }
  .memory-lightbox-image {
    max-width: 100%;
    max-height: 100%;
  }
  .lightbox-story {
    width: 80%;
  }
  .lightbox-metadata {
    position: fixed;
    left: 30px;
    bottom: 30px;
  }
  div {
    font-family: 'Montserrat', sans-serif;
    // color: white !important;
  }

</style>

<script lang="ts">
import { date } from 'quasar'
import { Component, Vue } from 'vue-property-decorator'
import ReviewNoteTable from '../components/ReviewNoteTable.vue';
import PerformanceReviewTable from '../components/PerformanceReviewTable.vue';
import { AudioRetrieve, ImageRetrieve, StoryRetrieve, VideoRetrieve } from '../store/types'

@Component({
  components: { PerformanceReviewTable, ReviewNoteTable }
})
export default class Dashboard extends Vue {
  private currentIndex = -1
  private title = ''
  private memories: Array<AudioRetrieve|ImageRetrieve|StoryRetrieve|VideoRetrieve> = []
  private carousel = false
  private slide = ''
  private carouselAutoplay = false
  private showSpinner = true

  private readableDate(unformattedDate: Date): string {
    return date.formatDate(unformattedDate, 'M/D/YYYY')
  }

  private images(): Array<ImageRetrieve> {
    let images: Array<ImageRetrieve> = this.$store.getters['memoriesModule/images'].results // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-assignment
    images.forEach(image => {
      image.key = `image-${image.pk}`
      image.type = 'image'
    })
    return images
  }

  private stories(): Array<StoryRetrieve> {
    let stories: Array<StoryRetrieve> = this.$store.getters['memoriesModule/stories'].results // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-assignment
    stories.forEach(story => {
      story.key = `story-${story.pk}`
      story.type = 'story'
    })
    return stories
  }

  private videos(): Array<VideoRetrieve> {
    let videos: Array<VideoRetrieve> = this.$store.getters['memoriesModule/videos'].results // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-assignment
    videos.forEach(video => {
      video.key = `video-${video.pk}`
      video.type = 'video'
    })
    return videos
  }

  private audio(): Array<AudioRetrieve> {
    let audio: Array<AudioRetrieve> = this.$store.getters['memoriesModule/audio'].results // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-assignment
    audio.forEach(audio => {
      audio.key = `audio-${audio.pk}`
      audio.type = 'audio'
    })
    return audio
  }

  private getMemories() {
    let memories: Array<AudioRetrieve|ImageRetrieve|StoryRetrieve|VideoRetrieve> = []
    Promise.all([
      this.$store.dispatch('memoriesModule/getImages'),
      this.$store.dispatch('memoriesModule/getStories'),
      this.$store.dispatch('memoriesModule/getVideos'),
      this.$store.dispatch('memoriesModule/getAudio')
    ]).then(() => {
      this.images().forEach(imageMemory => memories.push(imageMemory))
      this.stories().forEach(storyMemory => memories.push(storyMemory))
      this.videos().forEach(videoMemory => memories.push(videoMemory))
      this.audio().forEach(audioMemory => memories.push(audioMemory))
      this.memories = memories
        .map((a) => ({sort: Math.random(), value: a}))
        .sort((a, b) => a.sort - b.sort)
        .map((a) => a.value)
      this.showSpinner = false
    })
    .catch(e => {
      console.error('Error getting all memories:', e)
    })
  }

  private openCarousel(key: string): void {
    this.slide = key
    this.carousel = true
  }

  mounted() {
    // this.retrieveImages()
    //   .catch(e => {
    //     console.error('Error retrieving images:', e)
    //   })
    this.getMemories()
  }
};
</script>
