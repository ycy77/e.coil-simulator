---
entity_id: "gene.b1216"
entity_type: "gene"
name: "chaA"
source_database: "NCBI RefSeq"
source_id: "gene-b1216"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1216"
  - "chaA"
---

# chaA

`gene.b1216`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1216`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chaA (gene.b1216) is a gene entity. It encodes chaA (protein.P31801). Encoded protein function: FUNCTION: Sodium exporter that functions mainly at alkaline pH (PubMed:8021217, PubMed:8496184, PubMed:9518629). Can also function as a potassium/proton and calcium/proton antiporter at alkaline pH (PubMed:16687400, PubMed:18342619, PubMed:8021217, PubMed:8496184). Does not play a major role in calcium export (PubMed:18342619). The K(+)/H(+) antiporter activity may enable E.coli to adapt to K(+) salinity stress and to maintain K(+) homeostasis (PubMed:16687400). {ECO:0000269|PubMed:16687400, ECO:0000269|PubMed:18342619, ECO:0000269|PubMed:8021217, ECO:0000269|PubMed:8496184, ECO:0000269|PubMed:9518629}. EcoCyc product frame: CHAA-MONOMER. Genomic coordinates: 1270749-1271849. EcoCyc protein note: ChaA is an Na+/K+:proton antiporter which contributes to growth at alkaline pH.E. coli appears to contain a number of transporters which mediate active proton uptake for alkaline pH homeostasis including CPLX0-7629 "NhaA" (the prominent Na+:H+ antiporter), NHAB-MONOMER "NhaB", CMR-MONOMER "MdfA" and YJIO-MONOMER "MdtM", each of which may function under varying conditions of external pH and cation composition (see ) Overexpression of chaA complements the Na+ sensitivity of E. coli strain EP432 (ΔEG10652 "nhaA" ΔEG11392 "nhaB) which lacks Na+:H+ antiporter activity . The E...

## Biological Role

Repressed by glaR (protein.P37338). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31801|protein.P31801]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=chaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004082,ECOCYC:EG11753,GeneID:945790`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1270749-1271849:-; feature_type=gene
