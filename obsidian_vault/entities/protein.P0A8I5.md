---
entity_id: "protein.P0A8I5"
entity_type: "protein"
name: "trmB"
source_database: "UniProt"
source_id: "P0A8I5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trmB trmI yggH b2960 JW2927"
---

# trmB

`protein.P0A8I5`

## Static

- Type: `protein`
- Source: `UniProt:P0A8I5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of N(7)-methylguanine at position 46 (m7G46) in tRNA. {ECO:0000255|HAMAP-Rule:MF_01057, ECO:0000269|PubMed:12730187}. tRNA m7G46 methyltransferase (TrmB) catalyzes methylation of N(7) of the G46 nucleotide in the variable loop of tRNAs . tRNAs carry multiple modifications, often in nearby nucleotide residues. TrmB methyltransferase and tRNA binding activity is not influenced by prior tRNA modification in the T loop . Depending on the specific tRNA, lack of prior m7G modification at position 46 reduces 3-(3-amino-3-carboxypropyl)uridine (acp3U) modification at position 47 by G7349-MONOMER TapT . Based on a homology model of TrmB, potential catalytic residues have been mutagenized; kinetic analysis of the mutant enzymes showed a significant reduction in methyltransferase activity for most mutants . Crystal structures of TrmB alone and in complexes with SAM and SAH have been solved, showing that the enzyme adopts a modified Rossmann fold . TrmB has a relatively low affinity for tRNA, with a KD of about 6 μM in the absence of its cofactor SAM , but the affinity is significantly increased in the presence of SAM ( (KD of ~2 μM) . A trmB mutant lacks m7G in tRNAs, but has no significant growth defect . As was demonstrated for other bacterial species, an E...

## Biological Role

Catalyzes S-adenosyl-L-methionine:tRNA guanine N7-methyltransferase; (reaction.R00600), TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN (reaction.ecocyc.TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN).

## Annotation

FUNCTION: Catalyzes the formation of N(7)-methylguanine at position 46 (m7G46) in tRNA. {ECO:0000255|HAMAP-Rule:MF_01057, ECO:0000269|PubMed:12730187}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00600|reaction.R00600]] `KEGG` `database` - via EC:2.1.1.33
- `catalyzes` --> [[reaction.ecocyc.TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN|reaction.ecocyc.TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2960|gene.b2960]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8I5`
- `KEGG:ecj:JW2927;eco:b2960;ecoc:C3026_16200;`
- `GeneID:93779031;947448;`
- `GO:GO:0008176; GO:0030488; GO:0036265; GO:0043527; GO:0106004`
- `EC:2.1.1.33`

## Notes

tRNA (guanine-N(7)-)-methyltransferase (EC 2.1.1.33) (tRNA (guanine(46)-N(7))-methyltransferase) (tRNA(m7G46)-methyltransferase)
