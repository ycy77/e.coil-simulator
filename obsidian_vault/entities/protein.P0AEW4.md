---
entity_id: "protein.P0AEW4"
entity_type: "protein"
name: "cpdA"
source_database: "UniProt"
source_id: "P0AEW4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cpdA icc b3032 JW3000"
---

# cpdA

`protein.P0AEW4`

## Static

- Type: `protein`
- Source: `UniProt:P0AEW4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes cAMP to 5'-AMP. Plays an important regulatory role in modulating the intracellular concentration of cAMP, thereby influencing cAMP-dependent processes. Specific for cAMP. {ECO:0000255|HAMAP-Rule:MF_00905, ECO:0000269|PubMed:8810311}. cAMP phosphodiesterase hydrolyzes the important regulatory molecule cAMP and may thus influence the level of transcription of genes regulated by cAMP-CRP . Usage of the unusual translation start codon UUG has been confirmed by amino-terminal sequencing of the purified protein and may be involved in translational regulation of CpdA expression . CpdA is the founding member of the Class III family of 3',5'-cyclic nucleotide phosphodiesterases . Expression of CpdA appears to be itself catabolite-repressed . A cpdA mutant has slightly increased intracellular levels of cAMP . Overexpression of cpdA leads to increased resistance to hypochlorous acid stress due to derepression of rpoS and to increased persister cell formation due to reduced indole production . CpdA: "cyclic AMP phosphodiesterase" Reviews: The publication by reporting that CpdA's low affinity for cAMP compared to the dissociation constant of cAMP from CRP suggests that the enzyme does not have a major impact on cAMP concentration in E. coli has been retracted .

## Biological Role

Catalyzes adenosine 3',5'-phosphate 5'-nucleotidohydrolase (reaction.R00191), RXN0-5038 (reaction.ecocyc.RXN0-5038). Bound by Fe2+ (molecule.C14818).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Hydrolyzes cAMP to 5'-AMP. Plays an important regulatory role in modulating the intracellular concentration of cAMP, thereby influencing cAMP-dependent processes. Specific for cAMP. {ECO:0000255|HAMAP-Rule:MF_00905, ECO:0000269|PubMed:8810311}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00191|reaction.R00191]] `KEGG` `database` - via EC:3.1.4.53
- `catalyzes` --> [[reaction.ecocyc.RXN0-5038|reaction.ecocyc.RXN0-5038]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3032|gene.b3032]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEW4`
- `KEGG:ecj:JW3000;eco:b3032;ecoc:C3026_16560;`
- `GeneID:93778961;947515;`
- `GO:GO:0000166; GO:0004115; GO:0008198`
- `EC:3.1.4.53`

## Notes

3',5'-cyclic adenosine monophosphate phosphodiesterase CpdA (3',5'-cyclic AMP phosphodiesterase) (cAMP phosphodiesterase) (EC 3.1.4.53)
