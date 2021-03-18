import { GetterTree } from 'vuex';
import { StateInterface } from '../../index';
import { UserStateInterface } from './state';

const getters: GetterTree<UserStateInterface, StateInterface> = {
  getEmployeeProfile: state => state.profile,
  isProfileLoaded: state => !!state.profile.username
};

export default getters;
