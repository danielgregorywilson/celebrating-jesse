import { ActionTree } from 'vuex';
import { StateInterface } from '../../index';
import { MemoriesStateInterface } from './state';
import axios from 'axios';

const actions: ActionTree<MemoriesStateInterface, StateInterface> = {
  getImages: ({ commit }, page: number) => {
    return new Promise<void>((resolve, reject) => {
      axios({ url: `${ process.env.API_URL }api/v1/images?page=${ page }` }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
        .then(resp => {
          commit('setImages', resp);
          resolve();
        })
        .catch(e => {
          console.error('Error getting all images:', e)
          reject();
        });
      });
  },
  getStories: ({ commit }, page: number) => {
    return new Promise<void>((resolve, reject) => {
      axios({ url: `${ process.env.API_URL }api/v1/stories?page=${ page }` }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
        .then(resp => {
          commit('setStories', resp);
          resolve();
        })
        .catch(e => {
          console.error('Error getting all stories:', e)
          reject();
        });
    });
  },
  getVideos: ({ commit }, page: number) => {
    return new Promise<void>((resolve, reject) => {
      axios({ url: `${ process.env.API_URL }api/v1/videos?page=${ page }` }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
        .then(resp => {
          commit('setVideos', resp);
          resolve();
        })
        .catch(e => {
          console.error('Error getting all videos:', e)
          reject();
        });
    });
  },
  getAudio: ({ commit }, page: number) => {
    return new Promise<void>((resolve, reject) => {
      axios({ url: `${ process.env.API_URL }api/v1/audio?page=${ page }` }) // eslint-disable-line @typescript-eslint/restrict-template-expressions
        .then(resp => {
          commit('setAudio', resp);
          resolve();
        })
        .catch(e => {
          console.error('Error getting all audio:', e)
          reject();
        });
    });
  },
  toggleShowInfoContainer: ({ commit }) => {
    return new Promise<void>((resolve) => {
      commit('toggleShowInfoContainer')
      resolve()
    });
  },
};

export default actions;
