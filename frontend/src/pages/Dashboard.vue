<template>
  <q-page class="q-pa-md" id="page">
    <q-spinner-cube
      size="5.5em"
      class="cube-spinner"
      v-if="showSpinner"
    />
    <div class="row q-gutter-md justify-left q-pb-md">
      <div v-if="showInfo && !showSpinner" class="info-container row items-center justify-center">
        <q-avatar id="close-info" color="primary" text-color="white" icon="close" @click="toggleShowInfoContainer" />
        <div id="info-layout-large" class="row q-gutter-md">
          <img class="col q-pl-sm" src="../assets/jesse-wedding.jpg" id="info-photo" />
          <div class="col q-pr-sm q-gutter-sm" style="height: 150px">
            <div class="memory-container-text q-pt-xl">Hi there, my name is Dan, and this is my friend, Jesse.</div>
            <div class="memory-container-text">Jesse was one of the first, best things that ever happened to me, and I was hoping to spend the rest of my life with him.</div>
            <div class="memory-container-text">Since I don't get to do that, I am hope you will join me in sharing some of your memories of Jesse.</div>
            <div class="memory-container-text">Use the navigation panel to register for an account, and upload your memories of him. If you have any trouble, please <a class="text-primary" href="mailto:celebratingjessecontact@gmail.com">contact me</a>.</div>
          </div>
        </div>
        <div id="info-layout-small" class="row q-gutter-md">
          <div class="col">
            <div class="row justify-center">
              <img id="info-photo" src="../assets/jesse-wedding.jpg" />
            </div>
            <div class="row q-pa-md">
              <div class="memory-container-text">Hi there, my name is Dan, and this is my friend, Jesse.</div>
              <div class="memory-container-text">Jesse was one of the first, best things that ever happened to me, and I was hoping to spend the rest of my life with him.</div>
              <div class="memory-container-text">Since I don't get to do that, I am hope you will join me in sharing some of your memories of Jesse.</div>
              <div class="memory-container-text">Use the navigation panel to register for an account, and upload your memories of him. If you have any trouble, please <a class="text-primary" href="mailto:celebratingjessecontact@gmail.com">contact me</a>.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
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

    <div class="q-pa-lg flex flex-center">
      <q-pagination
        v-if="!showSpinner"
        v-model="currentPage"
        :max="maxPages()"
        @input="showInfo = false; getMemories(currentPage)"
      />
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
          <div class="lightbox-metadata-inline q-mt-sm">
            <div v-if="memory.title">{{ memory.title }}</div>
            <div v-if="memory.description" class="row">{{ memory.description }}</div>
            <div v-if="memory.date" class="row">Date: {{ memory.date }}</div>
            <div v-if="memory.age && memory.age != -1" class="row">Age: {{ memory.age }}</div>
            <div class="row">Uploaded by {{ memory.uploaded_by_name }} on {{ readableDate(memory.uploaded_at) }}</div>
          </div>
          <q-card class="lightbox-metadata-card">
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
  .info-container {
    width: 1314px;
    height: 516px;
    background-color: $darker;
    border-radius: 5px;

    #close-info {
      position: absolute;
      left: 25px;
      top: 25px;
    }

    #info-photo {
      height: 487px;
      object-fit: contain;
    }
  }
  #info-layout-large {
    display: flex;
  }
  #info-layout-small {
    display: none;
  }
  @media (max-width: 1555px) {
    // 4 boxes wide
    .info-container {
      width: 1048px;
      height: 516px;
    }
  }
  @media (max-width: 1289px) {
    // 3 boxes wide
    .info-container {
      width: 782px;
      height: 516px;
    }
  }
  @media (max-width: 813px) {
    // 2 boxes wide
    .info-container {
      width: 516px;
      height: 410px;

      #info-photo {
        height: 410px;
      }
    }
  }
  @media (max-width: 547px) {
    // 1 box wide
    .info-container {
      width: 250px;
      height: 622px;
    }
    #info-layout-large {
      display: none;
    }
    #info-layout-small {
      display: flex;
    }
    #info-photo {
      height: 250px !important;
    }
    .lightbox-metadata-card {
      display: none;
    }
    .lightbox-metadata-inline {
      display: block !important;
    }
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
  .lightbox-metadata-card {
    position: fixed;
    left: 30px;
    bottom: 30px;
  }
  .lightbox-metadata-inline {
    display: none;
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
  private showInfo = true
  
  private currentPage = 1

  private maxPages() {
    return this.$store.getters['memoriesModule/maxPages'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
  }

  private readableDate(unformattedDate: Date): string {
    return date.formatDate(unformattedDate, 'M/D/YYYY')
  }

  private getShowInfoContainer(): void {
    this.showInfo = this.$store.getters['memoriesModule/showInfoContainer'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-assignment
  }

  private toggleShowInfoContainer(): void {
    this.$store.dispatch('memoriesModule/toggleShowInfoContainer')
      .then(() => this.getShowInfoContainer())
      .catch((err) => console.log(err))
  }

  private images(): Array<ImageRetrieve> {
    let images: Array<ImageRetrieve> = this.$store.getters['memoriesModule/images'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-assignment
    images.forEach(image => {
      image.key = `image-${image.pk}`
      image.type = 'image'
    })
    return images
  }

  private stories(): Array<StoryRetrieve> {
    let stories: Array<StoryRetrieve> = this.$store.getters['memoriesModule/stories'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-assignment
    stories.forEach(story => {
      story.key = `story-${story.pk}`
      story.type = 'story'
    })
    return stories
  }

  private videos(): Array<VideoRetrieve> {
    let videos: Array<VideoRetrieve> = this.$store.getters['memoriesModule/videos'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-assignment
    videos.forEach(video => {
      video.key = `video-${video.pk}`
      video.type = 'video'
    })
    return videos
  }

  private audio(): Array<AudioRetrieve> {
    let audio: Array<AudioRetrieve> = this.$store.getters['memoriesModule/audio'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-assignment
    audio.forEach(audio => {
      audio.key = `audio-${audio.pk}`
      audio.type = 'audio'
    })
    return audio
  }

  private getMemories(page: number) {
    let memories: Array<AudioRetrieve|ImageRetrieve|StoryRetrieve|VideoRetrieve> = []
    this.showSpinner = true
    
    // Only get memories of types that we have more of to get
    let getNextPageImages = this.$store.getters['memoriesModule/totalImagePages'] >= page // eslint-disable-line @typescript-eslint/no-unsafe-member-access
    let getNextPageStories = this.$store.getters['memoriesModule/totalStoryPages'] >= page // eslint-disable-line @typescript-eslint/no-unsafe-member-access
    let getNextPageVideos = this.$store.getters['memoriesModule/totalVideoPages'] >= page // eslint-disable-line @typescript-eslint/no-unsafe-member-access
    let getNextPageAudio = this.$store.getters['memoriesModule/totalAudioPages'] >= page // eslint-disable-line @typescript-eslint/no-unsafe-member-access

    let getters = []
    if (getNextPageImages) {
      getters.push(this.$store.dispatch('memoriesModule/getImages', page))
    }
    if (getNextPageStories) {
      getters.push(this.$store.dispatch('memoriesModule/getStories', page))
    }
    if (getNextPageVideos) {
      getters.push(this.$store.dispatch('memoriesModule/getVideos', page))
    }
    if (getNextPageAudio) {
      getters.push(this.$store.dispatch('memoriesModule/getAudio', page))
    }
    
    Promise.all(getters)
    .then(() => {
      if (getNextPageImages) {
        this.images().forEach(imageMemory => memories.push(imageMemory))
      }
      if (getNextPageStories) {
        this.stories().forEach(storyMemory => memories.push(storyMemory))
      }
      if (getNextPageVideos) {
        this.videos().forEach(videoMemory => memories.push(videoMemory))
      }
      if (getNextPageAudio) {
        this.audio().forEach(audioMemory => memories.push(audioMemory))
      }
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
    this.getMemories(1)
    this.getShowInfoContainer()
  }
};
</script>
