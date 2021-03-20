<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title id="header">
          Celebrating Jesse
        </q-toolbar-title>

        <div>Built with Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-page-container id="page">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<style lang="scss">
  #header {
    font-family: 'Satisfy', cursive;
    font-size: 42px;
  }
  #page {
    font-family: 'Montserrat', sans-serif;
    font-weight: medium;
  }
</style>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class AuthLayout extends Vue{}
</script>
