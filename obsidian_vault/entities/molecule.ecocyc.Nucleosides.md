---
entity_id: "molecule.ecocyc.Nucleosides"
entity_type: "small_molecule"
name: "a nucleoside"
source_database: "EcoCyc"
source_id: "Nucleosides"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "nucleoside"
---

# a nucleoside

`molecule.ecocyc.Nucleosides`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Nucleosides`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

Nucleosides are glycosylamines consisting of Bases bound to a CPD0-1110 ribose or 2-DEOXYRIBOSE sugar via a β-glycosidic linkage. The nucleosides are called Ribonucleosides ribonucleosides when the sugar is CPD0-1110 ribose, and Deoxy-Ribonucleosides deoxyribonucleosides when it is 2-DEOXYRIBOSE. Common Ribonucleosides ribonucleosides include CYTIDINE, URIDINE, ADENOSINE, GUANOSINE and INOSINE. Examples of Deoxy-Ribonucleosides deoxyribonucleosides include THYMIDINE and DEOXYADENOSINE. When nucleosides are phosphorylated on the sugar's primary alcohol group, the resulting phosphonucleosides are called Nucleotides nucleotides. Nucleosides are glycosylamines consisting of Bases bound to a CPD0-1110 ribose or 2-DEOXYRIBOSE sugar via a β-glycosidic linkage. The nucleosides are called Ribonucleosides ribonucleosides when the sugar is CPD0-1110 ribose, and Deoxy-Ribonucleosides deoxyribonucleosides when it is 2-DEOXYRIBOSE. Common Ribonucleosides ribonucleosides include CYTIDINE, URIDINE, ADENOSINE, GUANOSINE and INOSINE. Examples of Deoxy-Ribonucleosides deoxyribonucleosides include THYMIDINE and DEOXYADENOSINE. When nucleosides are phosphorylated on the sugar's primary alcohol group, the resulting phosphonucleosides are called Nucleotides nucleotides.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 4 reaction(s).

## Annotation

Nucleosides are glycosylamines consisting of Bases bound to a CPD0-1110 ribose or 2-DEOXYRIBOSE sugar via a β-glycosidic linkage. The nucleosides are called Ribonucleosides ribonucleosides when the sugar is CPD0-1110 ribose, and Deoxy-Ribonucleosides deoxyribonucleosides when it is 2-DEOXYRIBOSE. Common Ribonucleosides ribonucleosides include CYTIDINE, URIDINE, ADENOSINE, GUANOSINE and INOSINE. Examples of Deoxy-Ribonucleosides deoxyribonucleosides include THYMIDINE and DEOXYADENOSINE. When nucleosides are phosphorylated on the sugar's primary alcohol group, the resulting phosphonucleosides are called Nucleotides nucleotides.

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.RXN-14473|reaction.ecocyc.RXN-14473]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7199|reaction.ecocyc.RXN0-7199]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-108|reaction.ecocyc.TRANS-RXN-108]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-468|reaction.ecocyc.TRANS-RXN0-468]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7199|reaction.ecocyc.RXN0-7199]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-108|reaction.ecocyc.TRANS-RXN-108]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-468|reaction.ecocyc.TRANS-RXN0-468]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACID-PHOSPHATASE-RXN|reaction.ecocyc.ACID-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Nucleosides`
- `LIGAND-CPD:C00801`
- `CHEBI:33838`
