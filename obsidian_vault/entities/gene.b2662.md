---
entity_id: "gene.b2662"
entity_type: "gene"
name: "gabT"
source_database: "NCBI RefSeq"
source_id: "gene-b2662"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2662"
  - "gabT"
---

# gabT

`gene.b2662`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2662`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gabT (gene.b2662) is a gene entity. It encodes gabT (protein.P22256). Encoded protein function: FUNCTION: Pyridoxal phosphate-dependent enzyme that catalyzes transamination between primary amines and alpha-keto acids. Catalyzes the transfer of the amino group from gamma-aminobutyrate (GABA) to alpha-ketoglutarate (KG) to yield succinic semialdehyde (SSA) and glutamate (PubMed:15723541, PubMed:30498244). Thereby functions in a GABA degradation pathway that allows some E.coli strains to utilize GABA as a nitrogen source for growth (PubMed:12446648). Also catalyzes the conversion of 5-aminovalerate to glutarate semialdehyde, as part of a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). {ECO:0000269|PubMed:12446648, ECO:0000269|PubMed:15723541, ECO:0000269|PubMed:30498244}. EcoCyc product frame: GABATRANSAM-MONOMER. Genomic coordinates: 2792735-2794015. EcoCyc protein note: 4-aminobutyrate aminotransferase is the initial enzyme of one of two 4-aminobutyrate (GABA) degradation pathways . It belongs to the aminotransferase subgroup II of pyridoxal 5'-phosphate (PLP)-dependent enzymes . GabT also functions as a 5-aminovalerate aminotransferase during degradation of L-lysine . Crystal structures of the free and inhibitor-bound enzyme and various point mutants have been reported...

## Biological Role

Repressed by glaR (protein.P37338). Activated by lrp (protein.P0ACJ0), crp (protein.P0ACJ8), nac (protein.Q47005).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22256|protein.P22256]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=gabT; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=gabT; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=gabT; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=gabT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008760,ECOCYC:EG10361,GeneID:948067`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2792735-2794015:+; feature_type=gene
