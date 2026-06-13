---
entity_id: "protein.P0AG67"
entity_type: "protein"
name: "rpsA"
source_database: "UniProt"
source_id: "P0AG67"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:342903}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpsA ssyF b0911 JW0894"
---

# rpsA

`protein.P0AG67`

## Static

- Type: `protein`
- Source: `UniProt:P0AG67`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:342903}.

## Enriched Summary

FUNCTION: Required for translation of most natural mRNAs except for leaderless mRNA (PubMed:12068815, PubMed:17376482, PubMed:24339747, PubMed:7003157, PubMed:9677288). Binds mRNA upstream of the Shine-Dalgarno (SD) sequence and helps it bind to the 30S ribosomal subunit; acts as an RNA chaperone to unfold structured mRNA on the ribosome but is not essential for mRNAs with strong SDs and little 5'-UTR structure, thus it may help fine-tune which mRNAs that are translated (PubMed:24339747). Unwinds dsRNA by binding to transiently formed ssRNA regions; binds about 10 nucleotides (PubMed:22908248). Has a preference for polypyrimidine tracts (PubMed:778845). Negatively autoregulates its own translation (PubMed:2120211). {ECO:0000269|PubMed:12068815, ECO:0000269|PubMed:15340139, ECO:0000269|PubMed:1712292, ECO:0000269|PubMed:17376482, ECO:0000269|PubMed:2120211, ECO:0000269|PubMed:22908248, ECO:0000269|PubMed:24339747, ECO:0000269|PubMed:7003157, ECO:0000269|PubMed:778845, ECO:0000269|PubMed:9677288}.; FUNCTION: It is not clear if it plays a role in trans-translation (a process which rescues stalled ribosomes). Evidence for its role; binds to tmRNA with very high affinity, is required for binding of tmRNA to 30S subunit (PubMed:11101533, PubMed:15340139). Thought to play a role only in translation of the tmRNA in vitro (PubMed:17392345)...

## Biological Role

Component of 30S ribosomal subunit (complex.ecocyc.CPLX0-3953).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: Required for translation of most natural mRNAs except for leaderless mRNA (PubMed:12068815, PubMed:17376482, PubMed:24339747, PubMed:7003157, PubMed:9677288). Binds mRNA upstream of the Shine-Dalgarno (SD) sequence and helps it bind to the 30S ribosomal subunit; acts as an RNA chaperone to unfold structured mRNA on the ribosome but is not essential for mRNAs with strong SDs and little 5'-UTR structure, thus it may help fine-tune which mRNAs that are translated (PubMed:24339747). Unwinds dsRNA by binding to transiently formed ssRNA regions; binds about 10 nucleotides (PubMed:22908248). Has a preference for polypyrimidine tracts (PubMed:778845). Negatively autoregulates its own translation (PubMed:2120211). {ECO:0000269|PubMed:12068815, ECO:0000269|PubMed:15340139, ECO:0000269|PubMed:1712292, ECO:0000269|PubMed:17376482, ECO:0000269|PubMed:2120211, ECO:0000269|PubMed:22908248, ECO:0000269|PubMed:24339747, ECO:0000269|PubMed:7003157, ECO:0000269|PubMed:778845, ECO:0000269|PubMed:9677288}.; FUNCTION: It is not clear if it plays a role in trans-translation (a process which rescues stalled ribosomes). Evidence for its role; binds to tmRNA with very high affinity, is required for binding of tmRNA to 30S subunit (PubMed:11101533, PubMed:15340139). Thought to play a role only in translation of the tmRNA in vitro (PubMed:17392345). Evidence against its role; overexpression of whole protein or various S1 fragments inhibits translation, they have no effect on trans-translation, and an in vitro system with S1-less ribosomes performs trans-translation (PubMed:15340139, PubMed:17376482). In trans-translation Ala-aminoacylated transfer-messenger RNA (tmRNA, product of the ssrA gene; the 2 termini fold to resemble tRNA(Ala) while it encodes a short internal open reading frame (the tag peptide)) acts like a tRNA, entering the A-site of the ribosome and displacing the stalled mRNA (which is subsequently degraded). The ribosome then switches to translate the ORF on the tmRNA, the nascent peptide is terminated with the 'tag peptide' encoded by the tmRNA and thus targeted for degradation. {ECO:0000269|PubMed:11101533, ECO:0000269|PubMed:15340139, ECO:0000269|PubMed:17376482, ECO:0000269|PubMed:17392345}.; FUNCTION: (Microbial infection) During infection by bacteriophage Qbeta, part of the viral RNA-dependent RNA polymerase complex; this subunit is required for RNA replication initiation activity during synthesis of (-) strand RNA from the (+) strand genomic RNA but not for (+) strand synthesis from the (-) strand (PubMed:25122749, PubMed:6358207). Binds an approximately 70 nucleotide RNA internal to the viral replicase gene (the M-site) (PubMed:25122749). Others have reported it is not involved in RNA replication initiation but rather in termination of RNA synthesis and is required for termination whether it is the (+) or (-) strand that is being synthesized (PubMed:23653193). {ECO:0000269|PubMed:23653193, ECO:0000269|PubMed:25122749, ECO:0000269|PubMed:6358207, ECO:0000269|PubMed:816798}.; FUNCTION: (Microbial infection) During infection by bacteriophage T4, plays a significant role in substrate choice by viral endoribonuclease RegB. {ECO:0000269|PubMed:17130171}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (4)

- `activates` --> [[gene.b1818|gene.b1818]] `RegulonDB|EcoCyc` `S` - regulator=RpsA; target=manY; function=+ | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `activates` --> [[gene.b3261|gene.b3261]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `is_component_of` --> [[complex.ecocyc.CPLX0-3953|complex.ecocyc.CPLX0-3953]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0911|gene.b0911]] `RegulonDB|EcoCyc` `S` - regulator=RpsA; target=rpsA; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0911|gene.b0911]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG67`
- `KEGG:ecj:JW0894;eco:b0911;ecoc:C3026_05615;`
- `GeneID:86863436;93776506;945536;`
- `GO:GO:0000028; GO:0002181; GO:0003723; GO:0003727; GO:0003729; GO:0003735; GO:0005737; GO:0006412; GO:0016020; GO:0022627; GO:2000766; GO:2000767`

## Notes

Small ribosomal subunit protein bS1 (30S ribosomal protein S1) (Bacteriophage Q beta RNA-directed RNA polymerase subunit I)
