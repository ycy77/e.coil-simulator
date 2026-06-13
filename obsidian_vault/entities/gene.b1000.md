---
entity_id: "gene.b1000"
entity_type: "gene"
name: "cbpA"
source_database: "NCBI RefSeq"
source_id: "gene-b1000"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1000"
  - "cbpA"
---

# cbpA

`gene.b1000`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1000`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cbpA (gene.b1000) is a gene entity. It encodes cbpA (protein.P36659). Encoded protein function: FUNCTION: DNA-binding protein that preferentially recognizes a curved DNA sequence. It is probably a functional analog of DnaJ; displays overlapping activities with DnaJ, but functions under different conditions, probably acting as a molecular chaperone in an adaptive response to environmental stresses other than heat shock. Lacks autonomous chaperone activity; binds native substrates and targets them for recognition by DnaK. Its activity is inhibited by the binding of CbpM. EcoCyc product frame: EG12193-MONOMER. Genomic coordinates: 1062855-1063775. EcoCyc protein note: CbpA has similarity to DnaJ and functions as a co-chaperone with DnaK in vitro . CbpA binds to curved DNA in vitro; binding is not sequence-specific . CbpA is an irregularly distributed nucleoid associated protein . Binding of CbpA to DNA inhibits co-chaperone activity in vitro; DNA binding and co-chaperone activity is inhibited by EG12194-MONOMER "CbpM" in vitro and in vivo . CbpA forms either a monomer or dimer in solution ; CbpA forms large aggregates when bound to plasmid DNA and protects against degradation by nucleases . CbpM disrupts CbpA-DNA aggregates in vitro...

## Biological Role

Repressed by fis (protein.P0A6R3), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36659|protein.P36659]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cbpA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=cbpA; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=cbpA; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003379,ECOCYC:EG12193,GeneID:947572`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1062855-1063775:-; feature_type=gene
