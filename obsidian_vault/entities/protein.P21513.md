---
entity_id: "protein.P21513"
entity_type: "protein"
name: "rne"
source_database: "UniProt"
source_id: "P21513"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:11134527}. Cell inner membrane {ECO:0000269|PubMed:11134527, ECO:0000269|PubMed:22509045}; Peripheral membrane protein {ECO:0000269|PubMed:11134527, ECO:0000269|PubMed:22509045}; Cytoplasmic side {ECO:0000269|PubMed:11134527, ECO:0000269|PubMed:22509045}. Note=Associated with the cytoplasmic membrane via the N- and C-terminal regions. {ECO:0000269|PubMed:11134527, ECO:0000269|PubMed:22509045}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rne ams hmp1 b1084 JW1071"
---

# rne

`protein.P21513`

## Static

- Type: `protein`
- Source: `UniProt:P21513`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:11134527}. Cell inner membrane {ECO:0000269|PubMed:11134527, ECO:0000269|PubMed:22509045}; Peripheral membrane protein {ECO:0000269|PubMed:11134527, ECO:0000269|PubMed:22509045}; Cytoplasmic side {ECO:0000269|PubMed:11134527, ECO:0000269|PubMed:22509045}. Note=Associated with the cytoplasmic membrane via the N- and C-terminal regions. {ECO:0000269|PubMed:11134527, ECO:0000269|PubMed:22509045}.

## Enriched Summary

FUNCTION: Endoribonuclease that plays a central role in RNA processing and decay. Required for the maturation of 5S and 16S rRNAs and the majority of tRNAs. Also involved in the degradation of most mRNAs. Can also process other RNA species, such as RNAI, a molecule that controls the replication of ColE1 plasmid, and the cell division inhibitor DicF-RNA. It initiates the decay of RNAs by cutting them internally near their 5'-end. It is able to remove poly(A) tails by an endonucleolytic process. Required to initiate rRNA degradation during both starvation and quality control; acts after RNase PH (rph) exonucleolytically digests the 3'-end of the 16S rRNA (PubMed:27298395). Degradation of 16S rRNA leads to 23S rRNA degradation (PubMed:27298395). Processes the 3 tRNA(Pro) precursors immediately after the 3'-CCA to generate the mature ends (PubMed:27288443). {ECO:0000255|HAMAP-Rule:MF_00970, ECO:0000269|PubMed:10329633, ECO:0000269|PubMed:10762247, ECO:0000269|PubMed:11328869, ECO:0000269|PubMed:11871663, ECO:0000269|PubMed:16237448, ECO:0000269|PubMed:1691299, ECO:0000269|PubMed:1708438, ECO:0000269|PubMed:19889093, ECO:0000269|PubMed:27288443, ECO:0000269|PubMed:27298395, ECO:0000269|PubMed:6339234, ECO:0000269|PubMed:9732274}.; FUNCTION: Prefers 5'-monophosphorylated substrates over 5'-triphosphorylated substrates (PubMed:10762247)...

## Biological Role

Component of degradosome (complex.ecocyc.CPLX0-2381), ribonuclease E (complex.ecocyc.CPLX0-3461).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: Endoribonuclease that plays a central role in RNA processing and decay. Required for the maturation of 5S and 16S rRNAs and the majority of tRNAs. Also involved in the degradation of most mRNAs. Can also process other RNA species, such as RNAI, a molecule that controls the replication of ColE1 plasmid, and the cell division inhibitor DicF-RNA. It initiates the decay of RNAs by cutting them internally near their 5'-end. It is able to remove poly(A) tails by an endonucleolytic process. Required to initiate rRNA degradation during both starvation and quality control; acts after RNase PH (rph) exonucleolytically digests the 3'-end of the 16S rRNA (PubMed:27298395). Degradation of 16S rRNA leads to 23S rRNA degradation (PubMed:27298395). Processes the 3 tRNA(Pro) precursors immediately after the 3'-CCA to generate the mature ends (PubMed:27288443). {ECO:0000255|HAMAP-Rule:MF_00970, ECO:0000269|PubMed:10329633, ECO:0000269|PubMed:10762247, ECO:0000269|PubMed:11328869, ECO:0000269|PubMed:11871663, ECO:0000269|PubMed:16237448, ECO:0000269|PubMed:1691299, ECO:0000269|PubMed:1708438, ECO:0000269|PubMed:19889093, ECO:0000269|PubMed:27288443, ECO:0000269|PubMed:27298395, ECO:0000269|PubMed:6339234, ECO:0000269|PubMed:9732274}.; FUNCTION: Prefers 5'-monophosphorylated substrates over 5'-triphosphorylated substrates (PubMed:10762247). 5'-monophosphate-assisted cleavage requires at least 2 and preferably 3 or more unpaired 5'-terminal nucleotides. The optimal spacing between the 5' end and the scissile phosphate appears to be 8 nucleotides. Any sequence of unpaired nucleotides at the 5'-end is tolerated (PubMed:26694614). {ECO:0000269|PubMed:10762247, ECO:0000269|PubMed:26694614}.

## Pathways

- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2381|complex.ecocyc.CPLX0-2381]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4
- `is_component_of` --> [[complex.ecocyc.CPLX0-3461|complex.ecocyc.CPLX0-3461]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `represses` --> [[gene.b1084|gene.b1084]] `RegulonDB` `S` - regulator=ribonuclease E; target=rne; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1084|gene.b1084]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21513`
- `KEGG:ecj:JW1071;eco:b1084;ecoc:C3026_06565;`
- `GeneID:945641;`
- `GO:GO:0000049; GO:0000287; GO:0000967; GO:0003723; GO:0004521; GO:0004540; GO:0005737; GO:0006364; GO:0006396; GO:0006401; GO:0006402; GO:0008033; GO:0008270; GO:0008312; GO:0008995; GO:0009898; GO:0016020; GO:0017151; GO:0019843; GO:0042802; GO:0051259; GO:0051289; GO:0060090; GO:1902555; GO:1990061`
- `EC:3.1.26.12`

## Notes

Ribonuclease E (RNase E) (EC 3.1.26.12)
