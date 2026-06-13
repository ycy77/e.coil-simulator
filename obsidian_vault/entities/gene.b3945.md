---
entity_id: "gene.b3945"
entity_type: "gene"
name: "gldA"
source_database: "NCBI RefSeq"
source_id: "gene-b3945"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3945"
  - "gldA"
---

# gldA

`gene.b3945`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3945`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gldA (gene.b3945) is a gene entity. It encodes gldA (protein.P0A9S5). Encoded protein function: FUNCTION: Catalyzes the NAD-dependent oxidation of glycerol to dihydroxyacetone (glycerone) (PubMed:18179582, PubMed:3920199, PubMed:40950, PubMed:6365902, PubMed:8132480). Allows microorganisms to utilize glycerol as a source of carbon under anaerobic conditions (PubMed:18632294). In E.coli, an important role of GldA is also likely to regulate the intracellular level of dihydroxyacetone by catalyzing the reverse reaction, i.e. the conversion of dihydroxyacetone into glycerol (PubMed:18179582). Possesses a broad substrate specificity, since it is also able to oxidize 1,2-propanediol and several of its analogs, DL-2,3-butanediol and D-1-amino-2-propanol, and to reduce dihydroxyacetone, hydroxyacetone, glycolaldehyde and methylglyoxal into glycerol, 1,2-propanediol, ethylene glycol and lactaldehyde, respectively (PubMed:18179582, PubMed:3920199, PubMed:40950, PubMed:4385233, PubMed:6365902). {ECO:0000269|PubMed:18179582, ECO:0000269|PubMed:18632294, ECO:0000269|PubMed:3920199, ECO:0000269|PubMed:40950, ECO:0000269|PubMed:4385233, ECO:0000269|PubMed:6365902, ECO:0000269|PubMed:8132480}. EcoCyc product frame: GLYCDEH-MONOMER. Genomic coordinates: 4137932-4139035.

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9S5|protein.P0A9S5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012912,ECOCYC:EG11904,GeneID:948440`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4137932-4139035:-; feature_type=gene
