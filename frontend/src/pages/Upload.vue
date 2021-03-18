<template>
  <q-page class="q-pa-md">
    <p>Upload a memory of Jesse! Choose an image, video, audio recording, or story that you want to share.</p>
    <div class="q-gutter-sm">
      <q-radio v-model="type" val="image" label="Image" />
      <q-radio v-model="type" val="video" label="Video" />
      <q-radio v-model="type" val="audio" label="Audio" />
      <q-radio v-model="type" val="story" label="Story" />
    </div>
    <!-- <input v-if="type != 'story'" type="file" id="file_upload" name="file_upload"> -->
    <q-file v-if="type != 'story'" v-model="file" :label="type" />
    <q-input
      v-if="type == 'story'"
      v-model="story"
      filled
      type="textarea"
    />
    <q-input v-model="title" label="Title (optional)" />
    <q-input v-model="description" label="Description (optional)" />
    <p class="q-mt-lg">Date this took place. Alternatively, you can select Jesse's approximate age when this took place. (optional)</p>
    <div class="row">
      <q-date
        v-model="date"
        minimal
      />
      <div class="q-ml-md q-mt-xl">OR</div>
      <q-slider
          v-model="age"
          :min="0"
          :max="32"
          vertical
          reverse
          label-always
          :label-value="getAgeLabel()"
        />
    </div>
    <q-btn label="Upload" class="q-mt-lg" @click="upload()" :disable="!fieldsComplete() || uploading">
      <q-spinner-cube v-if="uploading" class="q-ml-sm" />
    </q-btn>

    <!-- Dialog to confirm memory uploaded -->
    <q-dialog v-model="showMemoryUploadedDialog" persistent>
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="check" color="primary" text-color="white" />
          <div class="col">
            <span class="q-ml-sm row">Your memory was successfully uploaded!</span>
            <span class="q-ml-sm row">If this is your first time uploading, it won't appear in the gallery until it has been approved.</span>
          </div>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Return to Gallery" color="primary" @click="navigateToGallery()" />
          <q-btn flat label="Upload Again" color="primary" @click="uploadAgain()" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<style scoped>

</style>

<script lang="ts">
import axios from 'axios';
import { Component, Vue } from 'vue-property-decorator'
import ReviewNoteTable from '../components/ReviewNoteTable.vue';
import PerformanceReviewTable from '../components/PerformanceReviewTable.vue';

@Component({
  components: { PerformanceReviewTable, ReviewNoteTable }
})
export default class Dashboard extends Vue {
  private type = 'image'
  private title = ''
  private description = ''
  private date = ''
  private age = -1

  private file = new File([''], '')
  private story = ''

  private uploading = false
  private showMemoryUploadedDialog = false

  private getAgeLabel(): string {
    if (this.age == -1) {
      return '0'
    } else {
      return this.age.toString()
    }
  }

  private fieldsComplete(): boolean {
    switch(this.type) {
      case 'image':
        return !!this.file.size
        break;
      case 'story':
        return !!this.story
      case 'video':
        return !!this.file.size
        break;
      case 'audio':
        return !!this.file.size
        break;
      default:
        // code block
    }
  }

  private upload(): void {
    this.uploading = true
    let fd = new FormData();
    fd.append('title', this.title)
    fd.append('description', this.description)
    if (!this.date) {
      this.date = ''
    }
    fd.append('date', this.date.split('/').join('-'))
    fd.append('age', this.age.toString())
    
    // const { type, title, description, date, file, story } = this
    switch(this.type) {
      case 'image':
        fd.append('image', this.file)
        axios({url: `${ process.env.API_URL }api/upload-image/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.uploading = false
            this.showMemoryUploadedDialog = true
          })
          .catch(e => {
            console.error('Error uploading image memory:', e)
          })
        break;
      case 'story':
        fd.append('story', this.story)
        axios({url: `${ process.env.API_URL }api/upload-story/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.uploading = false
            this.showMemoryUploadedDialog = true
          })
          .catch(e => {
            console.error('Error uploading story memory:', e)
          })
        break;
      case 'video':
        fd.append('video', this.file)
        axios({url: `${ process.env.API_URL }api/upload-video/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.uploading = false
            this.showMemoryUploadedDialog = true
          })
          .catch(e => {
            console.error('Error uploading video memory:', e)
          })
        break;
      case 'audio':
        fd.append('audio', this.file)
        axios({url: `${ process.env.API_URL }api/upload-audio/`, data: fd, method: 'POST' }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
          .then(() => {
            this.uploading = false
            this.showMemoryUploadedDialog = true
          })
          .catch(e => {
            console.error('Error uploading audio memory:', e)
          })
        break;
      default:
        // code block
    }
  }

  private navigateToGallery(): void {
    this.$router.push('/')
      .catch(e => {
        console.error('Error navigating to gallery:', e)
      })
  }

  private uploadAgain(): void {
    this.type = 'image'
    this.title = ''
    this.description = ''
    this.date = ''
    this.age = -1
    this.file = new File([''], '')
    this.story = ''
    this.showMemoryUploadedDialog = false
  }

};
</script>
