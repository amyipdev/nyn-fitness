import { writable } from 'svelte/store';
import type {GalleryWorkout} from './GalleryComponents/GalleryWorkout.js'

export const loginSelectionChoice = writable(0);
export const loginCompleted = writable(false);
export const switchHomeMode = writable(2);
export const currentWorkout = writable({wk_uuid:"",wk_name:"",descr:"",ytlink:"",duration:""})
