import { AudioRetrieveData, ImageRetrieveData, StoryRetrieveData, VideoRetrieveData } from 'src/store/types'
import Vue from 'vue'

import { MutationTree } from 'vuex'
import { MemoriesStateInterface } from './state'


const mutation: MutationTree<MemoriesStateInterface> = {
  setImages: (state, resp: {data: ImageRetrieveData}) => {
    Vue.set(state, 'totalImagePages', resp.data.total_pages)
    if (resp.data.total_pages > state.maxPages) {
      Vue.set(state, 'maxPages', resp.data.total_pages)
    }
    Vue.set(state, 'images', resp.data.results)
  },
  setStories: (state, resp: {data: StoryRetrieveData}) => {
    Vue.set(state, 'totalStoryPages', resp.data.total_pages)
    if (resp.data.total_pages > state.maxPages) {
      Vue.set(state, 'maxPages', resp.data.total_pages)
    }
    Vue.set(state, 'stories', resp.data.results)
  },
  setVideos: (state, resp: {data: VideoRetrieveData}) => {
    Vue.set(state, 'totalVideoPages', resp.data.total_pages)
    if (resp.data.total_pages > state.maxPages) {
      Vue.set(state, 'maxPages', resp.data.total_pages)
    }
    Vue.set(state, 'videos', resp.data.results)
  },
  setAudio: (state, resp: {data: AudioRetrieveData}) => {
    Vue.set(state, 'totalAudioPages', resp.data.total_pages)
    if (resp.data.total_pages > state.maxPages) {
      Vue.set(state, 'maxPages', resp.data.total_pages)
    }
    Vue.set(state, 'audio', resp.data.results)
  },
  toggleShowInfoContainer: (state) => {
    Vue.set(state, 'showInfoContainer', !state.showInfoContainer)
  }
};

export default mutation;
