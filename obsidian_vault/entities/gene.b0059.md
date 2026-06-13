---
entity_id: "gene.b0059"
entity_type: "gene"
name: "rapA"
source_database: "NCBI RefSeq"
source_id: "gene-b0059"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0059"
  - "rapA"
---

# rapA

`gene.b0059`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0059`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rapA (gene.b0059) is a gene entity. It encodes rapA (protein.P60240). Encoded protein function: FUNCTION: Transcription regulator that activates transcription by stimulating RNA polymerase (RNAP) recycling in case of stress conditions such as supercoiled DNA or high salt concentrations (PubMed:11751638). Probably acts by releasing the RNAP when it is trapped or immobilized on tightly supercoiled DNA (Probable) (PubMed:10801781). Does not activate transcription on linear DNA (PubMed:11751638). Probably not involved in DNA repair (Probable) (PubMed:10801781). Has RNAP-stimulated (d)ATPase activity (PubMed:9507009, PubMed:9614128, PubMed:10801781, PubMed:11751638); ATPase is not stimulated by DNA (PubMed:9507009, PubMed:9614128), no other (d)nucleotides are hydrolyzed (PubMed:9507009), no helicase activity has been detected (PubMed:9507009, PubMed:9614128). Binds to single-stranded DNA, RNA, double-stranded DNA, and DNA-RNA duplexes (PubMed:9507009). {ECO:0000269|PubMed:10801781, ECO:0000269|PubMed:11751638, ECO:0000269|PubMed:9507009, ECO:0000269|PubMed:9614128, ECO:0000305|PubMed:10801781}. EcoCyc product frame: EG11083-MONOMER. EcoCyc synonyms: yabA, hepA. Genomic coordinates: 60358-63264. EcoCyc protein note: RapA enables recycling of stalled RNA polymerases (RNAPs) and stimulates RNA synthesis in vitro...

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60240|protein.P60240]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rapA; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rapA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000198,ECOCYC:EG11083,GeneID:948523`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:60358-63264:-; feature_type=gene
