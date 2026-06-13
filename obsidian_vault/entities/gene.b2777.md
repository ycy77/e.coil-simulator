---
entity_id: "gene.b2777"
entity_type: "gene"
name: "queE"
source_database: "NCBI RefSeq"
source_id: "gene-b2777"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2777"
  - "queE"
---

# queE

`gene.b2777`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2777`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

queE (gene.b2777) is a gene entity. It encodes queE (protein.P64554). Encoded protein function: FUNCTION: Catalyzes the complex heterocyclic radical-mediated conversion of 6-carboxy-5,6,7,8-tetrahydropterin (CPH4) to 7-carboxy-7-deazaguanine (CDG), a step common to the biosynthetic pathways of all 7-deazapurine-containing compounds. {ECO:0000255|HAMAP-Rule:MF_00917}. EcoCyc product frame: G7443-MONOMER. EcoCyc synonyms: ygcF. Genomic coordinates: 2904747-2905418. EcoCyc protein note: The QueE ortholog of Bacillus subtilis catalyzes the 7-carboxy-7-deazaguanine synthase reaction of the PWY-6703 pathway . Deletion of queE results in absence of queuosine and epoxyqueuosine from cellular RNA . A transposon insertion mutant or in-frame deletion of queE suppresses the filamentation phenotype due to a strongly stimulated PhoQ/PhoP two-comPonent system , and overexpression of queE leads to cell filamentation . Transcription of queE is regulated by PhoP . QueE is cytoplasmic, but also shows specific localization to the Z ring in filamentous cells .

## Biological Role

Activated by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16), phoP (protein.P23836).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64554|protein.P64554]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=queE; function=+
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=queE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009101,ECOCYC:G7443,GeneID:947527`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2904747-2905418:-; feature_type=gene
