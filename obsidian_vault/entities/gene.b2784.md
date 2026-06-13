---
entity_id: "gene.b2784"
entity_type: "gene"
name: "relA"
source_database: "NCBI RefSeq"
source_id: "gene-b2784"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2784"
  - "relA"
---

# relA

`gene.b2784`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2784`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

relA (gene.b2784) is a gene entity. It encodes relA (protein.P0AG20). Encoded protein function: FUNCTION: In eubacteria ppGpp (guanosine 3'-diphosphate 5'-diphosphate) is a mediator of the stringent response which coordinates a variety of cellular activities in response to changes in nutritional abundance. This enzyme catalyzes the formation of pppGpp which is then hydrolyzed to form ppGpp. The second messengers ppGpp and c-di-GMP together control biofilm formation in response to translational stress; ppGpp represses biofilm formation while c-di-GMP induces it. ppGpp activates transcription of CsrA-antagonistic small RNAs CsrB and CsrC, which down-regulate CsrA's action on translation during the stringent response (PubMed:21488981). {ECO:0000269|PubMed:14622409, ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:21488981, ECO:0000269|PubMed:26051177}. EcoCyc product frame: RELA-MONOMER. EcoCyc synonyms: RC. Genomic coordinates: 2911417-2913651. EcoCyc protein note: RelA is a key enzyme involved in the stringent response of Escherichia coli to amino acid starvation. It activates the synthesis of the global regulatory molecules of the stringent response, ppGpp and pppGpp (referred to collectively as (p)ppGpp), via a ribosomal mechanism (see below). The amino acid sequence of RelA has been shown to be extensively related to that of SPOT-MONOMER...

## Biological Role

Repressed by hipB (protein.P23873). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), crp (protein.P0ACJ8), glnG (protein.P0AFB8), rpoN (protein.P24255).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG20|protein.P0AG20]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=relA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=relA; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=relA; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=relA; function=+
- `represses` <-- [[protein.P23873|protein.P23873]] `RegulonDB` `S` - regulator=HipB; target=relA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009125,ECOCYC:EG10835,GeneID:947244`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2911417-2913651:-; feature_type=gene
