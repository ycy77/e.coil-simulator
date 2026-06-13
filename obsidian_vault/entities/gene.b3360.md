---
entity_id: "gene.b3360"
entity_type: "gene"
name: "pabA"
source_database: "NCBI RefSeq"
source_id: "gene-b3360"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3360"
  - "pabA"
---

# pabA

`gene.b3360`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3360`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pabA (gene.b3360) is a gene entity. It encodes pabA (protein.P00903). Encoded protein function: FUNCTION: Part of a heterodimeric complex that catalyzes the two-step biosynthesis of 4-amino-4-deoxychorismate (ADC), a precursor of p-aminobenzoate (PABA) and tetrahydrofolate. In the first step, a glutamine amidotransferase (PabA) generates ammonia as a substrate that, along with chorismate, is used in the second step, catalyzed by aminodeoxychorismate synthase (PabB) to produce ADC. PabA converts glutamine into glutamate only in the presence of stoichiometric amounts of PabB. {ECO:0000269|PubMed:4914080, ECO:0000269|PubMed:7592344}. EcoCyc product frame: PABASYN-COMPII-MONOMER. Genomic coordinates: 3490266-3490829. EcoCyc protein note: PabA (component 2) provides the glutamine amidotransferase activity of the aminodeoxychorismate synthase complex . PabA functions as a glutaminase, but only when in complex with PabB . The reaction proceeds via formation of a covalent PabA-γ-glutamyl intermediate . Titration of PabA with PabB showed a gain of glutaminase activity that reached a plateau at a 1:1 ratio of PabA/PabB, suggesting that the effect of PabB is as a stoichiometric positive allosteric effector on the PabA subunit . The presence of chorismate allosterically stimulates the glutaminase activity of PabA further...

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00903|protein.P00903]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pabA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=pabA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010983,ECOCYC:EG10682,GeneID:947873`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3490266-3490829:-; feature_type=gene
