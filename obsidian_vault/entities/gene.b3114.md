---
entity_id: "gene.b3114"
entity_type: "gene"
name: "tdcE"
source_database: "NCBI RefSeq"
source_id: "gene-b3114"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3114"
  - "tdcE"
---

# tdcE

`gene.b3114`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3114`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tdcE (gene.b3114) is a gene entity. It encodes tdcE (protein.P42632). Encoded protein function: FUNCTION: Catalyzes the cleavage of 2-ketobutyrate to propionyl-CoA and formate. It can also use pyruvate as substrate. {ECO:0000269|PubMed:9484901}. EcoCyc product frame: KETOBUTFORMLY-MONOMER. EcoCyc synonyms: yhaS. Genomic coordinates: 3260124-3262418. EcoCyc protein note: The tdcE gene encodes a protein with both 2-oxobutanoate formate-lyase and pyruvate formate-lyase activities that is equally active with both substrates. TdcE is a glycyl radical enzyme, and its activity is dependent on the same PFLACTENZ-MONOMER that is associated with the pflB-encoded pyruvate formate-lyase . The 2-oxobutanoate formate-lyase (KFL) activity is part of an anaerobic pathway for degradation of L-threonine . Overexpression of tdcE can partially complement the growth defect of a pflB mutant under conditions of anaerobic growth on glucose . Expression of the tdcABCDEFG operon is normally under catabolite repression and induced under anaerobic growth conditions in the presence of L-threonine . A tdcE deletion mutant does not have an obvious growth defect ; later it was shown that a transposon insertion in tdcE leads to constitutive SOS expression...

## Biological Role

Activated by crp (protein.P0ACJ8), tdcA (protein.P0ACQ7), tdcR (protein.P11866).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42632|protein.P42632]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=tdcE; function=+
- `activates` <-- [[protein.P0ACQ7|protein.P0ACQ7]] `RegulonDB` `S` - regulator=TdcA; target=tdcE; function=+
- `activates` <-- [[protein.P11866|protein.P11866]] `RegulonDB` `S` - regulator=TdcR; target=tdcE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010242,ECOCYC:G7627,GeneID:947623`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3260124-3262418:-; feature_type=gene
