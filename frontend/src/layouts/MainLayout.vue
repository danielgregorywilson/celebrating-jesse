<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-dark text-primary" id="headerBar">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          id="menu-button"
          @click="leftDrawerOpen = !leftDrawerOpen"
          class="text-secondary"
        />
        <q-toolbar-title id="mainHeader">
          Celebrating Jesse - UNDER CONSTRUCTION
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer
      id="drawer"
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      :width=210
    >
      <div class="text-secondary">
        <q-list>
          <q-item
            clickable
            @click='gallery'
          >
            <q-item-section avatar>
              <q-icon name='collections' />
            </q-item-section>
            <q-item-section>
              <q-item-label>Gallery</q-item-label>
            </q-item-section>
          </q-item>
          <q-item
            clickable
            @click='register'
            v-if="!profileLoaded()"
          >
            <q-item-section avatar>
              <q-icon name='how_to_reg' />
            </q-item-section>
            <q-item-section>
              <q-item-label>Register</q-item-label>
            </q-item-section>
          </q-item>
          <q-item
            clickable
            @click='login'
            v-if="!profileLoaded()"
          >
            <q-item-section avatar>
              <q-icon name='login' />
            </q-item-section>
            <q-item-section>
              <q-item-label>Log In</q-item-label>
            </q-item-section>
          </q-item>

          <q-item v-if="profileLoaded()">
            <q-item-section avatar>
              <q-icon name='person' />
            </q-item-section>
            <q-item-section>
              <q-item-label v-if="profile().name">{{ profile().name }} </q-item-label>
              <q-item-label v-else>{{ profile().username }} </q-item-label>
            </q-item-section>
          </q-item>
          <q-item
            clickable
            @click='logout'
            v-if="profileLoaded()"
          >
            <q-item-section avatar>
              <q-icon name='west' />
            </q-item-section>
            <q-item-section>
              <q-item-label>Log Out</q-item-label>
            </q-item-section>
          </q-item>
          <hr class="drawer-divider"/>
          <!-- <q-item
            @click='filter'
          >
            <q-item-section avatar>
              <q-icon name='filter_list' />
            </q-item-section>
            <q-item-section>
              <q-item-label>Filter</q-item-label>
            </q-item-section>
          </q-item> -->
          <q-item
            clickable
            @click='upload'
            v-if="profileLoaded()"
          >
            <q-item-section avatar>
              <q-icon name='file_upload' />
            </q-item-section>
            <q-item-section>
              <q-item-label>Upload</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>



<style lang="scss">
  .q-drawer {
    background-color: $darker;

  }
  .drawer-divider {
    border: 1px solid $secondary;
  }
  #mainHeader {
    font-family: 'Satisfy', cursive;
    color: white !important;
    font-size: 42px;
  }
  #headerBar{
    background: linear-gradient(90deg, $dark 0%, $darkAlt 100%, ) !important;
  }
  #drawer {
    font-family: 'Montserrat', sans-serif;
    font-weight: medium;
    color: white !important;
  }
</style>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

interface LinkData {
  title: string;
  icon: string;
  link: string;
}

interface LayoutData {
  name: string
}

@Component({})
export default class MainLayout extends Vue{
  private leftDrawerOpen = false

  private name() {
    return this.$store.getters['userModule/getEmployeeProfile'].name // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
  }

  public profileLoaded(): boolean {
    return this.$store.getters['userModule/isProfileLoaded'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
  }

  public profile(): boolean {
    return this.$store.getters['userModule/getEmployeeProfile'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
  }

  public getCurrentUser(): void {
    if (!this.$store.getters['userModule/isProfileLoaded']) { // eslint-disable-line @typescript-eslint/no-unsafe-member-access
      this.$store.dispatch('userModule/userRequest')
        .catch(e => {
          console.error('Error getting user from store:', e)
        })
    }
  }

  public gallery(): void {
    this.$router.push('/')
      .catch(e => {
        console.error('Error navigating to gallery page', e)
      })
  }

  public register(): void {
    this.$router.push('/auth/register')
      .catch(e => {
        console.error('Error navigating to register page', e)
      })
  }

  public login(): void {
    this.$router.push({ name: 'login' })
      .catch(e => {
        console.error('Error navigating to register page', e)
      })
  }

  public logout(): void {
    this.$store.dispatch('authModule/authLogout')
    .catch(e => {
      console.error('Error logging out', e);
    })
  }

  public filter(): void {
    return
  }

  public upload(): void {
    this.$router.push('/upload')
      .catch(e => {
        console.error('Error navigating to upload page', e)
      })
  }

  mounted() {
    // this.getCurrentUser();
  }
};
</script>
