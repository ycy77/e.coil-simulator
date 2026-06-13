---
entity_id: "gene.b1476"
entity_type: "gene"
name: "fdnI"
source_database: "NCBI RefSeq"
source_id: "gene-b1476"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1476"
  - "fdnI"
---

# fdnI

`gene.b1476`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1476`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fdnI (gene.b1476) is a gene entity. It encodes fdnI (protein.P0AEK7). Encoded protein function: FUNCTION: Formate dehydrogenase allows E.coli to use formate as major electron donor during anaerobic respiration, when nitrate is used as electron acceptor. Subunit gamma is the cytochrome b556 component of the formate dehydrogenase-N, and also contains a menaquinone reduction site that receives electrons from the beta subunit (FdnH), through its hemes. Formate dehydrogenase-N is part of a system that generates proton motive force, together with the dissimilatory nitrate reductase (Nar). {ECO:0000269|PubMed:11884747}. EcoCyc product frame: FDNI-MONOMER. Genomic coordinates: 1551338-1551991. EcoCyc protein note: fdnI encodes the γ subunit of formate dehydrogenase-N (Fhd-N); it is an integral membrane protein with four transmembrane helices, which, together with the single transmembrane helix of FdnH and a cardiolipin molecule, form a tightly packed trimer in the inner membrane. The γ subunit contains two heme b groups - heme bP located towards the periplasmic side of the membrane and heme bC located towards the cytoplasmic face of the membrane - and a site for menaquinone reduction .

## Biological Role

Repressed by fnr (protein.P0A9E5), narP (protein.P31802). Activated by fnr (protein.P0A9E5), narL (protein.P0AF28).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEK7|protein.P0AEK7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=fdnI; function=-+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=fdnI; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=fdnI; function=-+
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=fdnI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004921,ECOCYC:EG11229,GeneID:946038`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1551338-1551991:+; feature_type=gene
