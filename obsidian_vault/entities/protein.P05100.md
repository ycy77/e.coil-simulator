---
entity_id: "protein.P05100"
entity_type: "protein"
name: "tag"
source_database: "UniProt"
source_id: "P05100"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tag b3549 JW3518"
---

# tag

`protein.P05100`

## Static

- Type: `protein`
- Source: `UniProt:P05100`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolysis of the deoxyribose N-glycosidic bond to excise 3-methyladenine from the damaged DNA polymer formed by alkylation lesions. {ECO:0000269|PubMed:3536912}. Alkylating agents such as N-methyl-N'-nitro-N-nitrosoguanidine (MNNG) or methyl methanesulfonate (MMS) can produce potentially mutagenic lesions in DNA. Alkylation damage may also occur spontaneously in living organisms through the action of methyl donors such as S-adenosylmethionine . The product of the tag gene in Escherichia coli is one of two (along with AlkA) 3-methyladenine-DNA-glycosylases present in the genome. Like AlkA, it acts preferentially on double-stranded DNA containing 3-methyladenine by catalyzing the hydrolysis of the N-glycosylic bonds linking the methylated base to the deoxyribose -phosphate backbone. This enzymatic action results in the formation of an apurinic (AP) site which requires further repair through the action of an AP endonuclease, DNA polymerase and DNA-ligase. Unlike AlkA, the tag gene product is not inducible through the adaptation response.

## Biological Role

Catalyzes RXN0-5189 (reaction.ecocyc.RXN0-5189).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

FUNCTION: Hydrolysis of the deoxyribose N-glycosidic bond to excise 3-methyladenine from the damaged DNA polymer formed by alkylation lesions. {ECO:0000269|PubMed:3536912}.

## Pathways

- `eco03410` Base excision repair (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5189|reaction.ecocyc.RXN0-5189]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3549|gene.b3549]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05100`
- `KEGG:ecj:JW3518;eco:b3549;ecoc:C3026_19240;`
- `GeneID:947137;`
- `GO:GO:0006284; GO:0006307; GO:0008725; GO:0046872`
- `EC:3.2.2.20`

## Notes

DNA-3-methyladenine glycosylase 1 (EC 3.2.2.20) (3-methyladenine-DNA glycosylase I, constitutive) (TAG I) (DNA-3-methyladenine glycosidase I) (DNA-3-methyladenine glycosylase I)
