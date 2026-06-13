---
entity_id: "gene.b1102"
entity_type: "gene"
name: "fhuE"
source_database: "NCBI RefSeq"
source_id: "gene-b1102"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1102"
  - "fhuE"
---

# fhuE

`gene.b1102`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1102`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fhuE (gene.b1102) is a gene entity. It encodes fhuE (protein.P16869). Encoded protein function: FUNCTION: Involved in the active transport across the outer membrane of iron complexed with linear hydroxamate siderophores coprogen, rhodotorulic acid and ferrioxamine B. Binds Fe-coprogen with high affinity, rhodotorulic acid to a lesser extent, and weakly to ferrioxamine B. Selective for planar siderophores. Does not use cyclic siderophores ferrichrome nor ferrioxamine E as substrates. {ECO:0000269|PubMed:31098021}. EcoCyc product frame: EG10306-MONOMER. Genomic coordinates: 1159362-1161551. EcoCyc protein note: FhuE is a protein which serves as a receptor for ferric-coprogen (a hydroxamate-type iron chelator) and ferric-rhodotorulic acid . Uptake into the periplasm is facilitated by TonB coupling of inner membrane energy to power specific uptake across the outer membrane . Coprogen iron uptake is dependent on tonB, exbB and fhuCDB . FhuE appears to have a preference for Δ-absolute configuration metal complexes . In the Transporter Classification Database FhuE is a member of the Outer Membrane Receptor (OMR) family

## Biological Role

Repressed by fur (protein.P0A9A9), glaR (protein.P37338). Activated by ygaV (protein.P77295).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16869|protein.P16869]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P77295|protein.P77295]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=fhuE; function=-
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=fhuE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003724,ECOCYC:EG10306,GeneID:945649`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1159362-1161551:-; feature_type=gene
