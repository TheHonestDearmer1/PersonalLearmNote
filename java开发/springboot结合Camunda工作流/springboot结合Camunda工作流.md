

在 Camunda BPMN 引擎中，`runtimeService.startProcessInstanceByKey` 和 `runtimeService.createProcessInstanceByKey` 是两种不同的方法，用于启动流程实例。它们之间的主要区别在于流程实例的创建和启动方式。

### `runtimeService.startProcessInstanceByKey`

这个方法用于直接启动一个流程实例，并立即执行流程定义中的第一个活动。它会直接启动流程，并不会停留在任何特定的活动中。

#### 语法

```java
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(String processDefinitionKey);
```

#### 参数

- `processDefinitionKey`: 流程定义的 key，即在 BPMN 文件中定义的 `id` 属性。

#### 示例

```java
Map<String, Object> variables = new HashMap<>();
variables.put("creditor", "武松");

ProcessInstance instance = runtimeService.startProcessInstanceByKey("invoice", variables);
```

### `runtimeService.createProcessInstanceByKey`

这个方法用于创建一个流程实例，但并不立即执行它。你可以使用这个方法来设置一些初始条件或变量，并在某些条件下手动执行流程。

#### 语法

```java
ProcessInstanceBuilder builder = runtimeService.createProcessInstanceByKey(String processDefinitionKey);
```

#### 参数

- `processDefinitionKey`: 流程定义的 key。

#### 示例

```java
ProcessInstanceBuilder builder = runtimeService.createProcessInstanceByKey("invoice");
builder.setVariable("creditor", "武松");
ProcessInstance instance = builder.execute();
```

### `createProcessInstanceByKey` 的高级用法

`createProcessInstanceByKey` 提供了更多的灵活性，允许你在创建流程实例时设置更多的属性，如启动特定的活动、设置变量等。

#### `startBeforeActivity`

这个方法允许你在流程实例中指定从哪个活动开始执行。

#### 示例

```java
ProcessInstanceWithVariables instance = runtimeService.createProcessInstanceByKey("invoice")
    .startBeforeActivity("UserTaskOne")
    .setVariable("creditor", "武磊")
    .executeWithVariablesInReturn();
```

### 总结

- **`startProcessInstanceByKey`**：立即启动流程实例，并执行流程定义的第一个活动。
- **`createProcessInstanceByKey`**：创建流程实例，但不立即执行。可以用来设置更多的属性（如变量、启动活动等），然后手动执行。

### 返回变量

当你使用 `executeWithVariablesInReturn` 方法时，它会返回一个 `ProcessInstanceWithVariables` 对象，这个对象包含了流程实例的 ID 和流程变量。

#### 示例

```java
ProcessInstanceWithVariables instanceWithVars = runtimeService.createProcessInstanceByKey("invoice")
    .startBeforeActivity("UserTaskOne")
    .setVariable("creditor", "武磊")
    .executeWithVariablesInReturn();

System.out.println(instanceWithVars.getProcessInstanceId());
System.out.println(instanceWithVars.getVariables());
```

通过这种方式，你可以获取流程实例的 ID 和所有流程变量，这对于后续处理非常有用。

希望这些信息能帮助你更好地理解和使用 Camunda BPMN 引擎中的流程启动和控制机制！如果有更多具体问题或需要进一步的帮助，请随时告知。

在上述示例中，“invoice”代表的是流程定义的键（`processDefinitionKey`）。这是指在 Camunda BPMN 引擎中已经部署并可用的一个流程定义的唯一标识符。

流程定义键通常是 BPMN 流程模型文件中的 `id` 属性值，或者是你部署流程定义时给定的名称。这个键用于在流程引擎中引用具体的流程定义。

### 如何查找流程定义键

如果你不知道流程定义键是什么，可以通过以下几种方式来查找：

1. **查看 BPMN 文件**：
   在 BPMN 文件中 `<bpmn:process>` 标签的 `id` 属性就是流程定义的键。

   ```xml
   <bpmn:process id="invoice" isExecutable="true">
   ```

2. **查询已部署的流程定义**：
   使用 Camunda Engine 的管理界面或者 API 查询已部署的流程定义。

   ```java
   List<ProcessDefinition> processDefinitions = repositoryService.createDeploymentQuery().list();
   for (ProcessDefinition pd : processDefinitions) {
       System.out.println(pd.getKey()); // 输出流程定义的键
   }
   ```

3. **使用 Camunda Cockpit 或 Admin 接口**：
   在 Camunda Cockpit 或者 Admin 接口中，可以看到已部署的所有流程定义及其详细信息，其中包括流程定义的键。

### 示例

假设你有一个名为 `InvoiceProcess.bpmn` 的流程文件，其中的流程定义如下：

```xml
<bpmn:process id="invoice" isExecutable="true">
    <!-- 流程定义细节 -->
</bpmn:process>
```

在这个例子中，“invoice”就是流程定义的键。

### 启动流程实例

当你使用 `startProcessInstanceByKey` 或者 `createProcessInstanceByKey` 方法时，你需要提供这个键来告诉流程引擎你应该启动哪一个流程定义的实例。

```java
// 假设你已经部署了名为 "invoice" 的流程定义
Map<String, Object> variables = new HashMap<>();
variables.put("creditor", "武松");

// 启动名为 "invoice" 的流程定义的实例
ProcessInstance instance = runtimeService.startProcessInstanceByKey("invoice", variables);
```

在这个例子中，流程定义键 “invoice” 被用来启动一个新的流程实例。流程引擎将查找名为 “invoice” 的流程定义，并使用提供的变量来启动流程实例。