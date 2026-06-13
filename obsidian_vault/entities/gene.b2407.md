---
entity_id: "gene.b2407"
entity_type: "gene"
name: "xapA"
source_database: "NCBI RefSeq"
source_id: "gene-b2407"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2407"
  - "xapA"
---

# xapA

`gene.b2407`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2407`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xapA (gene.b2407) is a gene entity. It encodes xapA (protein.P45563). Encoded protein function: FUNCTION: The purine nucleoside phosphorylases catalyze the phosphorolytic breakdown of the N-glycosidic bond in the beta-(deoxy)ribonucleoside molecules, with the formation of the corresponding free purine bases and pentose-1-phosphate. This protein can degrade all purine nucleosides including xanthosine, inosine and guanosine, but cannot cleave adenosine, deoxyadenosine or hypoxanthine arabinoside. Has a preference for the neutral over the monoanionic form of xanthosine. {ECO:0000269|PubMed:15808857, ECO:0000269|PubMed:3042752, ECO:0000269|PubMed:7007808, ECO:0000269|PubMed:7007809}. EcoCyc product frame: XANTHOSINEPHOSPHORY-MONOMER. EcoCyc synonyms: pndA. Genomic coordinates: 2524045-2524878.

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45563|protein.P45563]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=xapA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=xapA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007927,ECOCYC:G85,GeneID:946878`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2524045-2524878:-; feature_type=gene
