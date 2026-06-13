---
entity_id: "gene.b0569"
entity_type: "gene"
name: "nfrB"
source_database: "NCBI RefSeq"
source_id: "gene-b0569"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0569"
  - "nfrB"
---

# nfrB

`gene.b0569`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0569`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nfrB (gene.b0569) is a gene entity. It encodes nfrB (protein.P0AFA5). Encoded protein function: FUNCTION: Required for bacteriophage N4 adsorption. May be a component of the phage receptor. EcoCyc product frame: EG11739-MONOMER. Genomic coordinates: 590941-593178. EcoCyc protein note: NfrB is a C-DI-GMP-activated glycosyltransferase which produces an uncharacterized exopolysaccharide (termed N4 glycan receptor or NGR) that impedes flagellar motility and acts as an initial (primary) receptor for the lytic bacteriophage N4; nfrB is located together with EG11740 nfrA, encoding an outer membrane protein, and EG12448 ybcH encoding a periplasmic protein, and the three proteins likely constitute an exopolysaccharide production/secretion system . NfrB contains an N-terminal glycosyltransferase domain and a C-terminal MshEN domain that binds cyclic di-3',5'-guanylate with high affinity; the two domains are linked by two predicted alpha-helices which likely anchor NfrB in the inner membrane; binding of cyclic di-3',5'-guanylate to the MshEN domain allosterically activates glycosyltransferase activity . NfrB interacts directly with the G6972-MONOMER and this interaction provides a localized source of cyclic di-3',5'-guanylate...

## Biological Role

Repressed by nac (protein.Q47005). Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFA5|protein.P0AFA5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nfrB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001942,ECOCYC:EG11739,GeneID:945849`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:590941-593178:-; feature_type=gene
