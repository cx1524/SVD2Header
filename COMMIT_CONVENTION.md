# Git Commit 规范指南

## 概述

本文档定义了 SVD2Header 项目的 Git Commit 消息规范，基于 Conventional Commits 标准。

## Commit Message 格式

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### 1. 类型 (Type)

| 类型 | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat: 添加Cortex-M4处理器支持` |
| `fix` | 修复bug | `fix: 修复寄存器位域解析错误` |
| `docs` | 文档更新 | `docs: 更新README安装说明` |
| `style` | 代码格式调整 | `style: 格式化模板文件缩进` |
| `refactor` | 重构代码 | `refactor: 重构SVD解析器模块` |
| `test` | 测试相关 | `test: 添加中断处理单元测试` |
| `chore` | 构建/工具链 | `chore: 更新uv依赖版本` |
| `perf` | 性能优化 | `perf: 优化内存映射解析性能` |

### 2. 作用域 (Scope) - 可选

| 作用域 | 说明 | 示例 |
|--------|------|------|
| `parser` | SVD解析器相关 | `feat(parser): 添加中断向量表解析` |
| `templates` | J2模板文件 | `fix(templates): 修复内存映射模板错误` |
| `build` | 构建/打包 | `chore(build): 更新pyinstaller配置` |
| `docs` | 文档 | `docs: 添加API使用示例` |

### 3. 描述 (Description)

- 使用现在时态（"添加功能" 而非 "添加了功能"）
- 使用祈使句（"移动文件" 而非 "移动了文件"）
- 首字母不大写
- 结尾不加句号
- 不超过50个字符

### 4. 正文 (Body) - 可选

- 与主题行空一行
- 每行不超过72个字符
- 说明变更的动机和背景
- 使用列表格式说明具体变更

### 5. 页脚 (Footer) - 可选

- 引用相关issue：`Closes #123`
- 标记破坏性变更：`BREAKING CHANGE: 描述变更影响`

## 最佳实践示例

### 好的示例

```
feat(parser): 添加Cortex-M7处理器支持

- 新增Cortex-M7 SVD解析逻辑
- 添加对应的内存映射模板
- 更新测试用例覆盖新处理器

Closes #123
```

```
fix(templates): 修复寄存器位域对齐问题

修复在32位系统上寄存器位域解析时的内存对齐错误，
确保生成的C头文件符合ARM EABI标准。

BREAKING CHANGE: 位域结构体布局发生变化
```

### 应避免的写法

- ❌ `update: update something` （重复且无意义）
- ❌ `fix bug` （过于简单，缺乏上下文）
- ❌ `add new feature` （不具体）
- ❌ `修复了问题` （使用过去时态）

## 配置Git使用模板

设置commit模板：
```bash
git config commit.template .gitmessage
```

## 自动化工具

项目已配置commit-msg钩子，会自动验证commit message格式。

## 分支命名规范

- 功能分支：`feature/描述性名称`
- 修复分支：`fix/问题描述`
- 发布分支：`release/版本号`
- 热修复分支：`hotfix/紧急问题描述`

示例：
- `feature/cortex-m7-support`
- `fix/register-alignment-issue`
- `release/v1.2.0`