---
entity_id: "gene.b1635"
entity_type: "gene"
name: "gstA"
source_database: "NCBI RefSeq"
source_id: "gene-b1635"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1635"
  - "gstA"
---

# gstA

`gene.b1635`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1635`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gstA (gene.b1635) is a gene entity. It encodes gstA (protein.P0A9D2). Encoded protein function: FUNCTION: Catalyzes the conjugation of reduced glutathione (GSH) to a wide number of exogenous and endogenous hydrophobic electrophiles. Shows activity toward 1-chloro-2,4-dinitrobenzene (CDNB) and ethacrynic acid. Also possesses thiol:disulfide oxidoreductase activity, using GSH to reduce bis-(2-hydroxyethyl) disulfide (HEDS). Has a low level of glutathione-dependent peroxidase activity toward cumene hydroperoxide. Is important for defense against oxidative stress, probably via its peroxidase activity. {ECO:0000269|PubMed:17018556, ECO:0000269|PubMed:18778244, ECO:0000269|PubMed:2185038, ECO:0000269|PubMed:7798255}. EcoCyc product frame: GST-MONOMER. EcoCyc synonyms: gst. Genomic coordinates: 1714377-1714982. EcoCyc protein note: Glutathione S-transferase (Gst) acts as a detoxifying enzyme that is thought to protect the cell from foreign compounds. The enzyme is active toward 1-chloro-2,4-dinitrobenzene . In addition, it also has a low level of glutathione-dependent peroxidase activity toward cumene hydroperoxide as well as thiol:disulfide oxidoreductase activity using bis-(2-hydroxyethyl) disulfide . Crystal structures of Gst have been determined at 2.1 and 1.9 Å resolution . Based on the structural information, Cys10 and His106 are thought to be involved in catalysis...

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9D2|protein.P0A9D2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005473,ECOCYC:G6878,GeneID:945758`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1714377-1714982:+; feature_type=gene
