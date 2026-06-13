---
entity_id: "protein.P37664"
entity_type: "protein"
name: "yiaC"
source_database: "UniProt"
source_id: "P37664"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yiaC b3550 JW3519"
---

# yiaC

`protein.P37664`

## Static

- Type: `protein`
- Source: `UniProt:P37664`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: N-epsilon-lysine acetyltransferase that catalyzes acetylation of a large number of proteins. Overexpression inhibits motility. {ECO:0000269|PubMed:30352934}. YiaC is an Nε-lysine acetyltransferase that targets 391 unique lysine residues in 251 proteins . Overexpression of YiaC in an acetylation-gutted strain (ΔEG20173 G7350 EG11448 G6577) leads to the appearance of acetylated proteins in an anti-acetyllysine Western blot. Mutagenesis of a predicted catalytic residue in YiaC, Y115A, eliminates the acetylation signal observed with the wild-type protein . YiaC was the only GCN5-related N-acetyltransferase (GNAT) family protein that resulted in lactylation of lysines when overexpressed, as measured in whole E. coli cell lysates by immunoblotting with a pan-lysine lactylation (Kla) antibody. ΔyiaC experiments confirmed the lactylation by YiaC and found over 1000 unique lysine sites in 478 proteins. Kinetic analysis found that YiaC has strong binding affinity to both lactyl-CoA, formed by EG12432-MONOMER, and to acetyl-CoA (KD = 6.83 and 5.57, respectively) but did not bind to succinyl-CoA. YiaC's lactylation activity was found to be more efficient than its acetylation activity. Proteomics analysis of the lactylome of E...

## Biological Role

Catalyzes peptidyl-lysine N-lactoyltransferase (reaction.ecocyc.RXN-25385), RXN0-7160 (reaction.ecocyc.RXN0-7160).

## Annotation

FUNCTION: N-epsilon-lysine acetyltransferase that catalyzes acetylation of a large number of proteins. Overexpression inhibits motility. {ECO:0000269|PubMed:30352934}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-25385|reaction.ecocyc.RXN-25385]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7160|reaction.ecocyc.RXN0-7160]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3550|gene.b3550]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37664`
- `KEGG:ecj:JW3519;eco:b3550;ecoc:C3026_19245;`
- `GeneID:946460;`
- `GO:GO:0061733`
- `EC:2.3.1.-`

## Notes

Peptidyl-lysine N-acetyltransferase YiaC (EC 2.3.1.-) (KAT)
