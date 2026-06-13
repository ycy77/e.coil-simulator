---
entity_id: "gene.b3088"
entity_type: "gene"
name: "alx"
source_database: "NCBI RefSeq"
source_id: "gene-b3088"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3088"
  - "alx"
---

# alx

`gene.b3088`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3088`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alx (gene.b3088) is a gene entity. It encodes alx (protein.P42601). Encoded protein function: FUNCTION: Functions as a low-activity manganese exporter at alkaline pH (PubMed:38869303). Involved in manganese homeostasis (PubMed:29440394, PubMed:38869303). Alx-mediated manganese export serves as a primary protective mechanism that fine tunes the cytoplasmic manganese content, especially during alkaline stress (PubMed:38869303). Transport of Mn(2+) by Alx is unlikely to be accompanied by an H(+) antiport (PubMed:38869303). Alx does not participate in maintaining cellular pH (PubMed:38869303). {ECO:0000269|PubMed:29440394, ECO:0000269|PubMed:38869303}. EcoCyc product frame: G7607-MONOMER. EcoCyc synonyms: ygjT. Genomic coordinates: 3238580-3239545. EcoCyc protein note: Alx is a "low-activity" Mn2+ exporter with a role in manganese ion homeostasis at alkaline pH; Alx-mediated Mn2+ export prevents a build-up of intracellular Mn2+ under alkaline conditions . Previously Alx was predicted to be a membrane-bound redox modulator . Expression from the alx promoter is highly induced by growth at an external pH of 8.5 and above both aerobically and anaerobically; expression is repressed by low pH only under aerobic conditions . alx expression is repressed by paraquat...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42601|protein.P42601]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=alx; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010151,ECOCYC:G7607,GeneID:947607`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3238580-3239545:+; feature_type=gene
