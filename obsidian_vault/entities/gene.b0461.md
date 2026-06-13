---
entity_id: "gene.b0461"
entity_type: "gene"
name: "tomB"
source_database: "NCBI RefSeq"
source_id: "gene-b0461"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0461"
  - "tomB"
---

# tomB

`gene.b0461`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0461`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tomB (gene.b0461) is a gene entity. It encodes tomB (protein.P0AAR0). Encoded protein function: FUNCTION: Attenuates Hha toxicity and regulates biofilm formation. Binds to various coding and intergenic regions of genomic DNA. {ECO:0000269|PubMed:16317765, ECO:0000269|PubMed:18545668}. EcoCyc product frame: EG12429-MONOMER. EcoCyc synonyms: ybaJ. Genomic coordinates: 480334-480708. EcoCyc protein note: The tomB-hha operon may encode an antitoxin-toxin module. Expression of TomB diminishes the toxicity of Hha expression. Both TomB and Hha were found to bind certain coding and intergenic regions of the genome . Transcription of tomB is induced upon biofilm formation . TomB: "toxin overexpression modulator in biofilms"

## Biological Role

Activated by rpoD (protein.P00579), cpxR (protein.P0AE88), basR (protein.P30843), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAR0|protein.P0AAR0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tomB; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=tomB; function=+
- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=tomB; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=tomB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001596,ECOCYC:EG12429,GeneID:945106`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:480334-480708:-; feature_type=gene
