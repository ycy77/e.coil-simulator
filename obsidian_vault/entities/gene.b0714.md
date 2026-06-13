---
entity_id: "gene.b0714"
entity_type: "gene"
name: "nei"
source_database: "NCBI RefSeq"
source_id: "gene-b0714"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0714"
  - "nei"
---

# nei

`gene.b0714`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0714`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nei (gene.b0714) is a gene entity. It encodes nei (protein.P50465). Encoded protein function: FUNCTION: Involved in base excision repair of DNA damaged by oxidation or by mutagenic agents. Acts as a DNA glycosylase that recognizes and removes damaged bases. Has a preference for oxidized pyrimidines, such as thymine glycol, 5,6-dihydrouracil and 5,6-dihydrothymine. Acts on DNA bubble and 3'-fork structures, suggesting a role in replication-associated DNA repair. Has AP (apurinic/apyrimidinic) lyase activity and introduces nicks in the DNA strand. Cleaves the DNA backbone by beta-delta elimination to generate a single-strand break at the site of the removed base with both 3'- and 5'-phosphates. {ECO:0000269|PubMed:20031487}. EcoCyc product frame: G6383-MONOMER. Genomic coordinates: 745935-746726. EcoCyc protein note: Endo VIII (purified initially from E. coli strain BW435 containing an nth deletion) has both DNA N-glycosylase and class I AP lyase activities; Endo VIII shares substrate specificity with EG10662-MONOMER "Endo III" - the product of nth . nei nth double deletion mutants have a strong mutator phenotype indicating that a significant number of premutagenic pyrimidine lesions are not repaired when cells lack both Endo VIII and Endo III...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P50465|protein.P50465]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nei; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002433,ECOCYC:G6383,GeneID:945320`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:745935-746726:+; feature_type=gene
