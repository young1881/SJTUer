import { describe, expect, it } from "vitest";
import TodoList from "../TodoList.vue";
import TodoItem from "../TodoItem.vue";
import TodoApp from "../TodoApp.vue";
import {mount} from "@vue/test-utils";

// 测试TodoList渲染
describe("TodoList", ()=>{
    it("render", ()=>{
        const wrapper = mount(()=><TodoList/>);
        expect(wrapper.exists()).toBeTruthy();
    });
});
// 测试TodoItem渲染
describe("TodoItem", ()=>{
    it("render", ()=>{
        const wrapper = mount(()=><TodoItem/>);
        expect(wrapper.exists()).toBeTruthy();
    });
});
// 测试TodoApp渲染
describe("TodoApp", ()=>{
    it("render", ()=>{
        const wrapper = mount(()=><TodoApp/>);
        expect(wrapper.exists()).toBeTruthy();
    });
});

