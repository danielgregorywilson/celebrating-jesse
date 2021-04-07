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
}

const state: MemoriesStateInterface = {
  images: [],
  stories: [],
  videos: [],
  audio: [],
  showInfoContainer: true
};

export default state;
