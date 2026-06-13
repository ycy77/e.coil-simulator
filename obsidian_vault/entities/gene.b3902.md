---
entity_id: "gene.b3902"
entity_type: "gene"
name: "rhaD"
source_database: "NCBI RefSeq"
source_id: "gene-b3902"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3902"
  - "rhaD"
---

# rhaD

`gene.b3902`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3902`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhaD (gene.b3902) is a gene entity. It encodes rhaD (protein.P32169). Encoded protein function: FUNCTION: Catalyzes the reversible cleavage of L-rhamnulose-1-phosphate to dihydroxyacetone phosphate (DHAP) and L-lactaldehyde (PubMed:12962479). Also catalyzes the dephosphorylation of phospho-serine in vitro (PubMed:25848029). {ECO:0000269|PubMed:12962479, ECO:0000269|PubMed:25848029}. EcoCyc product frame: RHAMNULPALDOL-MONOMER. Genomic coordinates: 4093448-4094272. EcoCyc protein note: Rhamnulose-1-phosphate aldolase is a class II aldolase that catalyzes the third step in the L-rhamnose degradation pathway. The enzyme contains 2 molecules of zinc per enzyme complex . If cobalt or selected other divalent metal ions are artificially substituted for zinc, the enzyme has an oxygenase activity in the presence of dihydroxyacetone phosphate . The enzyme has been crystallized , and crystal structures have been solved . A catalytic mechanism was proposed based on results from site-directed mutagenesis in combination with structural information . Anisotropic mobility of the N-terminal "antenna domain" supports catalysis . Stereospecificity of RhaD has been investigated . For the aldol addition reaction, RhaD accepts a range of aldehydes in place of L-lactaldehyde; this property has been used for synthesis of a variety of compounds of interest...

## Biological Role

Activated by rpoD (protein.P00579), rhaS (protein.P09377).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32169|protein.P32169]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rhaD; function=+
- `activates` <-- [[protein.P09377|protein.P09377]] `RegulonDB` `C` - regulator=RhaS; target=rhaD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012731,ECOCYC:EG11866,GeneID:948401`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4093448-4094272:-; feature_type=gene
