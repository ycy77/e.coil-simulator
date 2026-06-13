---
entity_id: "gene.b3608"
entity_type: "gene"
name: "gpsA"
source_database: "NCBI RefSeq"
source_id: "gene-b3608"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3608"
  - "gpsA"
---

# gpsA

`gene.b3608`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3608`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gpsA (gene.b3608) is a gene entity. It encodes gpsA (protein.P0A6S7). Encoded protein function: FUNCTION: Catalyzes the reduction of the glycolytic intermediate dihydroxyacetone phosphate (DHAP) to sn-glycerol 3-phosphate (G3P), the key precursor for phospholipid synthesis (PubMed:28326, PubMed:355254, PubMed:4597451). Is able to use both NADPH and NADH with similar efficiency. Can also catalyze the reverse reaction in vitro (PubMed:28326). {ECO:0000269|PubMed:28326, ECO:0000269|PubMed:355254, ECO:0000269|PubMed:4597451}. EcoCyc product frame: GLYC3PDEHYDROGBIOSYN-MONOMER. Genomic coordinates: 3782642-3783661. EcoCyc protein note: Glycerol-3-phosphate dehydrogenase (GpsA) catalyzes the NAD(P)H-dependent reduction of the glycolytic intermediate dihydroxyacetone-phosphate to produce glycerol-3-phosphate, a precursor for the biosynthesis of phospholipids . GpsA activity is strongly inhibited in vitro by glycerol-3-phosphate, and it was shown that this inhibition does not involve dimer association or dissociation. A mutant version of the protein which is resistant to feedback inhibition has been studied . The enzyme is constitutively produced, and is present in the cell in low amounts. It was calculated that on average only about 1000 molecules are present per cell . GpsA did not show dehydrogenase activity in a high-throughput screen of purified proteins .

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6S7|protein.P0A6S7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gpsA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gpsA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011795,ECOCYC:EG20091,GeneID:948125`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3782642-3783661:-; feature_type=gene
