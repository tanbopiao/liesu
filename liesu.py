"""列宿（LIESU）· 算力单元（星槎）

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：算力单元（星槎）。

边界：本件为算子骨架 v0——接口先立、实现随进化轮补齐；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Liesu:
    """列宿（LIESU）算子骨架 v0。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "LIESU"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "liesu",
            "cn": "列宿",
            "code": self.CODE,
            "duty": "算力单元（星槎）",
            "mingwen": "星槎列布，算力如辉",
            "anchor": self.ANCHOR,
        }

    def allocate(self, task):
        """为任务分配星槎算力槽位（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("LIESU.allocate 骨架桩，候进化轮补齐")

    def report_capacity(self):
        """上报当前算力余量（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("LIESU.report_capacity 骨架桩，候进化轮补齐")
