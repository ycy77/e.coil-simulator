---
entity_id: "gene.b1224"
entity_type: "gene"
name: "narG"
source_database: "NCBI RefSeq"
source_id: "gene-b1224"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1224"
  - "narG"
---

# narG

`gene.b1224`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1224`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narG (gene.b1224) is a gene entity. It encodes narG (protein.P09152). Encoded protein function: FUNCTION: The nitrate reductase enzyme complex allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The alpha chain is the actual site of nitrate reduction. EcoCyc product frame: NARG-MONOMER. EcoCyc synonyms: chlC, narC. Genomic coordinates: 1279864-1283607. EcoCyc protein note: The α subunit of nitrate reductase A is the site of nitrate reduction; it contains the molybdenum cofactor CPD-15873 (bis-MGD and an FS0 CPD-7 [4Fe-4S] cluster . The assembly of FS0 in nitrate reductase A is a prerequisite for bis-MGD insertion . The enzyme-specific chaperone NARJ-MONOMER "NarJ" facilitates bis-MGD insertion within the apoenzyme complex; NarJ interacts specifically with NarG . NarG contains a vestigal twin-arginine leader sequence . NarG and NarH are significantly upregulated in a ΔCPLX0-245 Ahp strain compared to wild type and redox proteomics indicates that cysteine sites in peptides (NarGCys-292/NarHCys-217) are significantly reduced . nar: nitrate reductase; chl: chlorate resistant

## Biological Role

Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5), rob (protein.P0ACI0), narL (protein.P0AF28).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09152|protein.P09152]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=narG; function=+
- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=narG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004119,ECOCYC:EG10638,GeneID:945782`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1279864-1283607:+; feature_type=gene
