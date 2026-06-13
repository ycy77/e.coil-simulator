---
entity_id: "protein.P09030"
entity_type: "protein"
name: "xthA"
source_database: "UniProt"
source_id: "P09030"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xthA xth b1749 JW1738"
---

# xthA

`protein.P09030`

## Static

- Type: `protein`
- Source: `UniProt:P09030`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Major apurinic-apyrimidinic endonuclease of E.coli. It removes the damaged DNA at cytosines and guanines by cleaving on the 3'-side of the AP site by a beta-elimination reaction. It exhibits 3'-5'-exonuclease, 3'-phosphomonoesterase, 3'-repair diesterase and ribonuclease H activities. Exonuclease III (XthA) is the major apurinic/apyrimidinic (AP) endonuclease under normal growth conditions; Exonuclease III is a multifunctional enzyme, it displays physiologically important 3' phosphomonoesterase and 3' repair diesterase activity as well as 3' → 5' exonuclease and ribonuclease H activity. Exonuclease III (XthA) was first purified from E. coli strain B and characterised as a 'DNA phosphatase-exonuclease'; active on dsDNA, the enzyme displayed both exonuclease activity (releasing 5' mononucleotides sequentially from the 3'-hydroxyl end of DNA) and 3'-phosphatase activity (releasing inorganic phosphate from 3'-phosphoryl terminated DNA) . The enzyme (purified from a K-12 strain) requires Mg2+ or Mn2+ for optimal activity and is inhibited by Zn2+; it displays AP endonuclease activity, processive 3' → to 5' exodeoxyribonuclease activity which is specific for dsDNA, 3'-phosphatase activity, and it degrades the RNA strand of a synthetic RNA-DNA hybrid (RNase H activity)...

## Biological Role

Catalyzes 3.1.11.2-RXN (reaction.ecocyc.3.1.11.2-RXN), RXN-20410 (reaction.ecocyc.RXN-20410), RXN-20426 (reaction.ecocyc.RXN-20426), RXN-20429 (reaction.ecocyc.RXN-20429).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

FUNCTION: Major apurinic-apyrimidinic endonuclease of E.coli. It removes the damaged DNA at cytosines and guanines by cleaving on the 3'-side of the AP site by a beta-elimination reaction. It exhibits 3'-5'-exonuclease, 3'-phosphomonoesterase, 3'-repair diesterase and ribonuclease H activities.

## Pathways

- `eco03410` Base excision repair (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.3.1.11.2-RXN|reaction.ecocyc.3.1.11.2-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-20410|reaction.ecocyc.RXN-20410]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-20426|reaction.ecocyc.RXN-20426]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-20429|reaction.ecocyc.RXN-20429]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1749|gene.b1749]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09030`
- `KEGG:ecj:JW1738;eco:b1749;ecoc:C3026_09990;`
- `GeneID:93775963;946254;`
- `GO:GO:0003677; GO:0004519; GO:0004527; GO:0005829; GO:0006281; GO:0006974; GO:0008311; GO:0046872`
- `EC:3.1.11.2`

## Notes

Exodeoxyribonuclease III (EXO III) (Exonuclease III) (EC 3.1.11.2) (AP endonuclease VI)
