import { GetterTree } from 'vuex';
import { StateInterface } from '../../index';
import { MemoriesStateInterface } from './state';

const getters: GetterTree<MemoriesStateInterface, StateInterface> = {
  images: state => state.images,
  stories: state => state.stories,
  videos: state => state.videos,
  audio: state => state.audio,
  showInfoContainer: state => state.showInfoContainer,
  totalImagePages: state => state.totalImagePages,
  totalStoryPages: state => state.totalStoryPages,
  totalVideoPages: state => state.totalVideoPages,
  totalAudioPages: state => state.totalAudioPages,
  maxPages: state => state.maxPages // eslint-disable-line @typescript-eslint/no-unsafe-return
};

export default getters;
