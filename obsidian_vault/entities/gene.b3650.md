---
entity_id: "gene.b3650"
entity_type: "gene"
name: "spoT"
source_database: "NCBI RefSeq"
source_id: "gene-b3650"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3650"
  - "spoT"
---

# spoT

`gene.b3650`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3650`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

spoT (gene.b3650) is a gene entity. It encodes spoT (protein.P0AG24). Encoded protein function: FUNCTION: In eubacteria ppGpp (guanosine 3'-diphosphate 5'-diphosphate) is a mediator of the stringent response which coordinates a variety of cellular activities in response to changes in nutritional abundance. This enzyme catalyzes both the synthesis and degradation of ppGpp. The second messengers ppGpp and c-di-GMP together control biofilm formation in response to translational stress; ppGpp represses biofilm formation while c-di-GMP induces it. ppGpp activates transcription of CsrA-antagonistic small RNAs CsrB and CsrC, which down-regulate CsrA's action on translation during the stringent response (PubMed:21488981). {ECO:0000269|PubMed:14622409, ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:21488981}. EcoCyc product frame: SPOT-MONOMER. Genomic coordinates: 3822400-3824508. EcoCyc protein note: SpoT is a key enzyme involved in the stringent response in Escherichia coli. It is a bifunctional enzyme with both hydrolase and synthetase activities . The ppGpp hydrolase activity of SpoT has a major physiological role in ppGpp degradation and is inhibited under conditions of physiological stress. Its amino acid sequence has been shown to be extensively related to that of RelA . RelA is involved in the E...

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG24|protein.P0AG24]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011935,ECOCYC:EG10966,GeneID:948159`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3822400-3824508:+; feature_type=gene
