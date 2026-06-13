---
entity_id: "gene.b0756"
entity_type: "gene"
name: "galM"
source_database: "NCBI RefSeq"
source_id: "gene-b0756"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0756"
  - "galM"
---

# galM

`gene.b0756`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0756`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

galM (gene.b0756) is a gene entity. It encodes galM (protein.P0A9C3). Encoded protein function: FUNCTION: Mutarotase converts alpha-aldose to the beta-anomer. It is active on D-glucose, L-arabinose, D-xylose, D-galactose, maltose and lactose. EcoCyc product frame: ALDOSE1EPIM-MONOMER. Genomic coordinates: 787797-788837. EcoCyc protein note: Epimerization of the β anomer of galactose to the α anomer links the metabolism of lactose and galactose. Although the interconversion of α- and β-galactose is spontaneous in vitro, the reaction is largely dependent on the presence of galactose-1-epimerase in vivo . The enzymatic reaction appears to follow a bifunctional mechanism, a simultaneous attack of a nucleophilic and electrophilic group of the enzyme on the substrate. The reaction proceeds from the pyranose form via the open chain intermediate, producing either pyranose or furanose products . The histidine residues H104 and H175 are essential for catalytic activity . A catalytic mechanism has been proposed . When overexpressed, a small amount of galactose-1-epimerase also appears in the periplasm and cell supernatant . galM is required for utilization of galactose generated from lactose, but is not required for utilization of extracellular galactose .

## Biological Role

Repressed by galR (protein.P03024), hns (protein.P0ACF8), crp (protein.P0ACJ8), galS (protein.P25748). Activated by rpoD (protein.P00579), galR (protein.P03024), crp (protein.P0ACJ8), rpoS (protein.P13445), galS (protein.P25748).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9C3|protein.P0A9C3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=galM; function=+
- `activates` <-- [[protein.P03024|protein.P03024]] `RegulonDB` `C` - regulator=GalR; target=galM; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=galM; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=galM; function=+
- `activates` <-- [[protein.P25748|protein.P25748]] `RegulonDB` `S` - regulator=GalS; target=galM; function=-+
- `represses` <-- [[protein.P03024|protein.P03024]] `RegulonDB` `C` - regulator=GalR; target=galM; function=-+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=galM; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=galM; function=-+
- `represses` <-- [[protein.P25748|protein.P25748]] `RegulonDB` `S` - regulator=GalS; target=galM; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002566,ECOCYC:EG11698,GeneID:944943`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:787797-788837:-; feature_type=gene
