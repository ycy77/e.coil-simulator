---
entity_id: "gene.b4132"
entity_type: "gene"
name: "cadB"
source_database: "NCBI RefSeq"
source_id: "gene-b4132"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4132"
  - "cadB"
---

# cadB

`gene.b4132`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4132`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cadB (gene.b4132) is a gene entity. It encodes cadB (protein.P0AAE8). Encoded protein function: FUNCTION: Under acidic conditions, in the presence of lysine, functions as a cadaverine:lysine antiporter that facilitates the excretion of cadaverine and the uptake of lysine (PubMed:14982633, PubMed:1556085). At neutral pH, also catalyzes the uptake of cadaverine via a proton symport mechanism, however the physiological relevance of this uptake activity is probably negligible because the expression of cadB is low at neutral pH (PubMed:14982633). Cadaverine uptake activity is low at acidic pH (PubMed:14982633). {ECO:0000269|PubMed:14982633, ECO:0000269|PubMed:1556085}. EcoCyc product frame: CADB-MONOMER. Genomic coordinates: 4358697-4360031. EcoCyc protein note: CadB, a lysine:cadaverine antiporter and CadA, a lysine decarboxylase constitute a lysine-dependent acid resistance system (LDAR) which functions to protect the cell from mild acid stress; the LDAR system is one of a number of amino acid dependent AR mechanisms in E. coli (reviewed in ). CadA catalyzes the decarboxylation of lysine to cadaverine and CO2 (a process that counteracts acid stress through consumption of cytosolic protons) while CadB exchanges the internal product, cadaverine for the external substrate, L-lysine. Cadaverine accumulates in the external medium when cells are grown anaerobically at pH 5...

## Biological Role

Repressed by ompR (protein.P0AA16), hns (protein.P0ACF8). Activated by lrp (protein.P0ACJ0), cadC (protein.P23890).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAE8|protein.P0AAE8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=cadB; function=+
- `activates` <-- [[protein.P23890|protein.P23890]] `RegulonDB` `S` - regulator=CadC; target=cadB; function=+
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=cadB; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=cadB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013530,ECOCYC:EG10132,GeneID:948654`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4358697-4360031:-; feature_type=gene
