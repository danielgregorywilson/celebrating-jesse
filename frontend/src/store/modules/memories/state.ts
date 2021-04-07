export interface Image {
  pk: number
  image: string
}

export interface Story {
  pk: number
  story: string
}

export interface Video {
  pk: number
  video: string
}

export interface Audio {
  pk: number
  audio: string
}

export interface MemoriesStateInterface {
  images: Array<Image>
  stories: Array<Story>
  videos: Array<Video>
  audio: Array<Audio>
  showInfoContainer: boolean
  totalImagePages: number
  totalStoryPages: number
  totalVideoPages: number
  totalAudioPages: number
  maxPages: number
}

const state: MemoriesStateInterface = {
  images: [],
  stories: [],
  videos: [],
  audio: [],
  showInfoContainer: true,
  totalImagePages: 1,
  totalStoryPages: 1,
  totalVideoPages: 1,
  totalAudioPages: 1,
  maxPages: 1
};

export default state;
