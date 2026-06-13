---
entity_id: "protein.P04395"
entity_type: "protein"
name: "alkA"
source_database: "UniProt"
source_id: "P04395"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alkA aidA b2068 JW2053"
---

# alkA

`protein.P04395`

## Static

- Type: `protein`
- Source: `UniProt:P04395`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolysis of the deoxyribose N-glycosidic bond to excise 3-methyladenine, 3-methylguanine, 7-methylguanine, O2-methylthymine, and O2-methylcytosine from the damaged DNA polymer formed by alkylation lesions. The alkA gene product is known as 3-methyl-adenine-DNA glycosylase II and is induced by exposure to alkylating agents as part of the cell's adaptive response to damage caused by alkylation. The purified enzyme acts preferentially on dsDNA to remove 3-methyl-adenine and 3-methyl-guanine with equal efficiency and also removes, somewhat less efficiently, 7-methyl-adenine, 7-methyl-guanine, 2-methyl-thymine and their ethylated derivatives . AlkA is one of two (along with 3-methyl-adenine DNA glycosylase I, the tag gene product) glycosylases that remove 3-methyl-adenines. Glycosylase II differs in two ways: it can remove several other methylated bases besides 3-methyl-adenine and it is inducible to a 20-fold higher level in cells exposed to alkylating agents . Additional roles for AlkA were found through studies on removal of deaminated adenine residues and studies on repair of oxidative damage. AlkA was found to be the hypoxanthine DNA glycosylase in E. coli. Hypoxanthine is potentially mutagenic as it can result in A-T to G-C transition mutations upon replication...

## Biological Role

Catalyzes 3.2.2.21-RXN (reaction.ecocyc.3.2.2.21-RXN).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

FUNCTION: Hydrolysis of the deoxyribose N-glycosidic bond to excise 3-methyladenine, 3-methylguanine, 7-methylguanine, O2-methylthymine, and O2-methylcytosine from the damaged DNA polymer formed by alkylation lesions.

## Pathways

- `eco03410` Base excision repair (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.2.2.21-RXN|reaction.ecocyc.3.2.2.21-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2068|gene.b2068]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04395`
- `KEGG:ecj:JW2053;eco:b2068;ecoc:C3026_11630;`
- `GeneID:947371;`
- `GO:GO:0003905; GO:0005737; GO:0006281; GO:0006284; GO:0006285; GO:0006307; GO:0006974; GO:0008725; GO:0032131; GO:0043916`
- `EC:3.2.2.21`

## Notes

DNA-3-methyladenine glycosylase 2 (EC 3.2.2.21) (3-methyladenine-DNA glycosylase II, inducible) (TAG II) (DNA-3-methyladenine glycosidase II) (DNA-3-methyladenine glycosylase II)
