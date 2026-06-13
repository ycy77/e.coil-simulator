---
entity_id: "protein.P0AAD6"
entity_type: "protein"
name: "sdaC"
source_database: "UniProt"
source_id: "P0AAD6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sdaC dcrA b2796 JW2767"
---

# sdaC

`protein.P0AAD6`

## Static

- Type: `protein`
- Source: `UniProt:P0AAD6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Mediates the import of L-serine into the cell (PubMed:3129404, PubMed:8026499). Is energized by proton cotransport (PubMed:3129404). Promotes amino acid homeostasis during adaptation to glucose limitation (PubMed:31680488). May also be involved in ampicillin sensitivity (Probable). {ECO:0000269|PubMed:3129404, ECO:0000269|PubMed:31680488, ECO:0000269|PubMed:8026499, ECO:0000305|PubMed:8752353}.; FUNCTION: (Microbial infection) Involved in phage C1 and phage C6 infection (PubMed:12558182, PubMed:8752353). Participates in phage DNA transport pathways in cooperation with different outer membrane receptors, including FhuA and BtuB (PubMed:12558182). Is probably required in the second stage of phage adsorption, the DNA injection process. Participates in the formation or opening of diffusion channels through the outer membrane after phage adsorption (PubMed:12558182). {ECO:0000269|PubMed:12558182, ECO:0000269|PubMed:8752353}.; FUNCTION: (Microbial infection) May function as an inner membrane receptor of colicin V (ColV), a peptide antibiotic secreted by some members of the Enterobacteriaceae to kill closely related bacterial cells. {ECO:0000269|PubMed:15743941}. sdaC encodes a (probable) L-serine:proton symporter which mediates the uptake of L-serine...

## Biological Role

Catalyzes L-serine:proton symport (reaction.ecocyc.TRANS-RXN-71).

## Annotation

FUNCTION: Mediates the import of L-serine into the cell (PubMed:3129404, PubMed:8026499). Is energized by proton cotransport (PubMed:3129404). Promotes amino acid homeostasis during adaptation to glucose limitation (PubMed:31680488). May also be involved in ampicillin sensitivity (Probable). {ECO:0000269|PubMed:3129404, ECO:0000269|PubMed:31680488, ECO:0000269|PubMed:8026499, ECO:0000305|PubMed:8752353}.; FUNCTION: (Microbial infection) Involved in phage C1 and phage C6 infection (PubMed:12558182, PubMed:8752353). Participates in phage DNA transport pathways in cooperation with different outer membrane receptors, including FhuA and BtuB (PubMed:12558182). Is probably required in the second stage of phage adsorption, the DNA injection process. Participates in the formation or opening of diffusion channels through the outer membrane after phage adsorption (PubMed:12558182). {ECO:0000269|PubMed:12558182, ECO:0000269|PubMed:8752353}.; FUNCTION: (Microbial infection) May function as an inner membrane receptor of colicin V (ColV), a peptide antibiotic secreted by some members of the Enterobacteriaceae to kill closely related bacterial cells. {ECO:0000269|PubMed:15743941}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-71|reaction.ecocyc.TRANS-RXN-71]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2796|gene.b2796]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAD6`
- `KEGG:ecj:JW2767;eco:b2796;ecoc:C3026_15375;`
- `GeneID:93779202;947264;`
- `GO:GO:0005886; GO:0006865; GO:0015194; GO:0015293; GO:0015825; GO:0022857`

## Notes

Serine transporter SdaC (H(+)/L-serine symporter) (L-serine transport system)
