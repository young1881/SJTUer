import { describe, expect, it } from "vitest";
import Flipper from "../Flipper.vue";
import FlipClock from "../FlipClock.vue";
import poem from "../poem.vue";
import searchbox from "../searchbox.vue";
import weather from "../weather.vue";
import sidebar from "../sidebar.vue";
import websites from "../websites.vue";
import site from "../site.vue";


import {mount} from "@vue/test-utils";

// 测试Flipper渲染
describe("Flipper", ()=>{
    it("render", ()=>{
        const wrapper = mount(()=><Flipper/>);
        expect(wrapper.exists()).toBeTruthy();
    });
});
// 测试FlipClock渲染
describe("FlipClock", ()=>{
    it("render", ()=>{
        const wrapper = mount(()=><FlipClock/>);
        expect(wrapper.exists()).toBeTruthy();
    });
});

// 测试poem渲染
describe("poem", ()=>{
    it("render", ()=>{
        const wrapper = mount(()=><poem/>);
        expect(wrapper.exists()).toBeTruthy();
    });
});
// 测试searchbox渲染
describe("searchbox", ()=>{
    it("render", ()=>{
        const wrapper = mount(()=><searchbox/>);
        expect(wrapper.exists()).toBeTruthy();
    });
});
// 测试weather渲染
describe("weather", ()=>{
    it("render", ()=>{
        const wrapper = mount(()=><weather/>);
        expect(wrapper.exists()).toBeTruthy();
    });
});

// 测试websites渲染
describe("websites", ()=>{
    it("render", ()=>{
        const wrapper = mount(()=><websites/>);
        expect(wrapper.exists()).toBeTruthy();
    });
});
// 测试site渲染
describe("site", ()=>{
    it("render", ()=>{
        const wrapper = mount(()=><site/>);
        expect(wrapper.exists()).toBeTruthy();
    });
});



