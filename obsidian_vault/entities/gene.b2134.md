---
entity_id: "gene.b2134"
entity_type: "gene"
name: "pbpG"
source_database: "NCBI RefSeq"
source_id: "gene-b2134"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2134"
  - "pbpG"
---

# pbpG

`gene.b2134`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2134`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pbpG (gene.b2134) is a gene entity. It encodes pbpG (protein.P0AFI5). Encoded protein function: FUNCTION: Cell wall formation. May play a specialized role in remodeling the cell wall. Specifically hydrolyzes the DD-diaminopimelate-alanine bonds in high-molecular-mass murein sacculi. EcoCyc product frame: EG12015-MONOMER. EcoCyc synonyms: yohB, psv. Genomic coordinates: 2223938-2224870. EcoCyc protein note: pbpG encodes penicillin-binding protein 7 (PBP7) and it's cleavage product, penicillin-binding protein 8 (PBP8) . PBP8 is likely an artifact that results from contact with OmpT, an outer membrane protease, during purification procedures . PPB7 is a soluble, periplasmic protein that is loosely membrane associated; the protein is non-essential when cells are grown in rich or minimal media under typical laboratory conditions . Purified PBP7/8 is a penicillin-sensitive DD endopeptidase with a preference for cleaving the D-ala-m-DAP (4→3) cross link in high-molecular mass sacculi; PBP7/8 has minor LD-endopeptidase activity and no apparent carboxypeptidase activity . Purified PBP7 cleaves 4→3 cross-links specifically and has no activity on 3→3 (m-DAP-m-DAP) cross-links . PBP7/8 binds to EG10950-MONOMER (Slt70) in vitro; PBP7/8 stimulates Slt70 activity in vitro . Loss of PBP7 accentuates the morphological abnormality of a mutant that lacks CPLX0-8252 PBP5...

## Biological Role

Repressed by soxS (protein.P0A9E2), marA (protein.P0ACH5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFI5|protein.P0AFI5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A9E2|protein.P0A9E2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB|EcoCyc` `S` - regulator=MarA; target=pbpG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007050,ECOCYC:EG12015,GeneID:946662`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2223938-2224870:-; feature_type=gene
