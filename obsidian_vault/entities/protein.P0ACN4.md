---
entity_id: "protein.P0ACN4"
entity_type: "protein"
name: "allR"
source_database: "UniProt"
source_id: "P0ACN4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "allR glxA3 ybbU b0506 JW0494"
---

# allR

`protein.P0ACN4`

## Static

- Type: `protein`
- Source: `UniProt:P0ACN4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Negative regulator of allantoin and glyoxylate utilization operons. Binds to the gcl promoter and to the allS-allA intergenic region. Binding to DNA is abolished by glyoxylate. {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:12460564, ECO:0000269|PubMed:16546208}. AllR (for "allantoin repressor") regulates several genes involved in the anaerobic utilization of allantoin as a nitrogen source . Inhibition of allR expression by CRISPRi reduced cellular fitness under treatment with the antibiotic novobiocin . At very low concentrations of glyoxylate, AllR represses transcription from allAp, allSp, and gclp. A highly conserved region featuring an almost perfect palindromic sequence has been identified in gclp and in the intergenic region between the divergent promoters allAp and allSp. It has been proven that AllR binds to this region, and it has been proposed that it may interfere with RNA polymerase by steric hindrance or contact inhibition, thus repressing transcription. In the presence of glyoxylate (the coeffector molecule of this regulator), DNA binding by AllR is inhibited and transcription of the allantoin regulon is derepressed . AllR belongs to the IclR family. Members of this family of regulators feature a conserved domain architecture, with a DNA-binding motif in the N-terminal domain and a ligand-binding motif in the C-terminal domain...

## Biological Role

Component of AllR-allantoin (complex.ecocyc.CPLX0-8071), AllR-glyoxylate (complex.ecocyc.MONOMER0-2201).

## Annotation

FUNCTION: Negative regulator of allantoin and glyoxylate utilization operons. Binds to the gcl promoter and to the allS-allA intergenic region. Binding to DNA is abolished by glyoxylate. {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:12460564, ECO:0000269|PubMed:16546208}.

## Outgoing Edges (11)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8071|complex.ecocyc.CPLX0-8071]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER0-2201|complex.ecocyc.MONOMER0-2201]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0504|gene.b0504]] `RegulonDB` `C` - regulator=AllR; target=allS; function=-
- `represses` --> [[gene.b0505|gene.b0505]] `RegulonDB` `C` - regulator=AllR; target=allA; function=-
- `represses` --> [[gene.b0507|gene.b0507]] `RegulonDB` `C` - regulator=AllR; target=gcl; function=-
- `represses` --> [[gene.b0508|gene.b0508]] `RegulonDB` `C` - regulator=AllR; target=hyi; function=-
- `represses` --> [[gene.b0509|gene.b0509]] `RegulonDB` `C` - regulator=AllR; target=glxR; function=-
- `represses` --> [[gene.b0511|gene.b0511]] `RegulonDB` `C` - regulator=AllR; target=allW; function=-
- `represses` --> [[gene.b0512|gene.b0512]] `RegulonDB` `C` - regulator=AllR; target=allB; function=-
- `represses` --> [[gene.b0513|gene.b0513]] `RegulonDB` `C` - regulator=AllR; target=ybbY; function=-
- `represses` --> [[gene.b0514|gene.b0514]] `RegulonDB` `C` - regulator=AllR; target=glxK; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0506|gene.b0506]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACN4`
- `KEGG:ecj:JW0494;eco:b0506;ecoc:C3026_02485;`
- `GeneID:86863056;86945421;945333;`
- `GO:GO:0003677; GO:0003700; GO:0005829; GO:0006974; GO:0042802; GO:0045892`

## Notes

HTH-type transcriptional repressor AllR (Negative regulator of allantoin and glyoxylate utilization operons)
