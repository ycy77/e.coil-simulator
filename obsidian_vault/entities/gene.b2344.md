---
entity_id: "gene.b2344"
entity_type: "gene"
name: "fadL"
source_database: "NCBI RefSeq"
source_id: "gene-b2344"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2344"
  - "fadL"
---

# fadL

`gene.b2344`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2344`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fadL (gene.b2344) is a gene entity. It encodes fadL (protein.P10384). Encoded protein function: FUNCTION: Involved in translocation of long-chain fatty acids across the outer membrane. It is a receptor for the bacteriophage T2. FadL may form a specific channel. EcoCyc product frame: EG10280-MONOMER. EcoCyc synonyms: ttr. Genomic coordinates: 2461306-2462646. EcoCyc protein note: FadL is an outer membrane, ligand gated channel that functions in the uptake of long chain (C12-C18) fatty acids (LCFAs) . Exogenous long-chain fatty acids are first recognized at the surface of FadL by a low-affinity binding site, followed by diffusion to a high-affinity binding site within a barrel. This translocation displaces an N-terminus plug, opening the barrel and resulting in release of the substrate in the outer membrane. Mutations in FadL can be generated that distinguish regions required for binding from those required for transport . FadL binding affinity is highest for OLEATE-CPD and PALMITATE; no binding of the medium-chain acid CPD-3617 is detected . FadL crystal structures at 2.6 and 2.8 Å indicate that the protein forms a 14-stranded antiparallel β barrel. The amino terminus forms a small "hatch" domain which plugs the barrel on the extracellular side...

## Biological Role

Repressed by fadR (protein.P0A8V6), arcA (protein.P0A9Q1), rpoN (protein.P24255). Activated by DNA-binding transcriptional dual regulator LldR-S-lactate (complex.ecocyc.CPLX0-7689), lrp (protein.P0ACJ0), crp (protein.P0ACJ8), pdhR (protein.P0ACL9), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10384|protein.P10384]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[complex.ecocyc.CPLX0-7689|complex.ecocyc.CPLX0-7689]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=fadL; function=+
- `activates` <-- [[protein.P0ACL9|protein.P0ACL9]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=fadL; function=+
- `represses` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `C` - regulator=FadR; target=fadL; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=fadL; function=-
- `represses` <-- [[protein.P24255|protein.P24255]] `RegulonDB|EcoCyc` `S` - regulator=RpoN; target=fadL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007740,ECOCYC:EG10280,GeneID:946820`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2461306-2462646:+; feature_type=gene
