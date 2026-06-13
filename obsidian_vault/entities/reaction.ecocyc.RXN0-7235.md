---
entity_id: "reaction.ecocyc.RXN0-7235"
entity_type: "reaction"
name: "ETF:quinone oxidoreductase"
source_database: "EcoCyc"
source_id: "RXN0-7235"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ETF:quinone oxidoreductase

`reaction.ecocyc.RXN0-7235`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7235`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ETF:quinone oxidoreductases (ETF-QO) are membrane-associated proteins that accept electrons from electron-transfer flavoprotein at their iron-sulfur site and transfer them to quinone at their flavin-binding site . The first purified ETF-QO was obtained from beef heart mitochondria . The best characterized enzymes are those from human , pig liver , and the metabolically complex photosynthetic purple bacterium Rhodobacter sphaeroides, whose ETF-QO shows high homology to the human ETFDH . Mutations in ETF and ETF-QO that disrupt this reaction activity result in the human inborn error of metabolism disease multiple acyl-CoA dehydrogenation deficiency (MADD) . The electron transfer is actually carried out as two one-electron transfers from ETF FAD semiquinone, instead of one two-electron transfer from a FAD hydroquinone . E. coli contains three ETFab-like gene pairs (ydiQR, ygcQR, and fixAB). FixAB is required for L-carnitine respiration via the CaiA dehydrogenase activity . The ETFs involved in E. coli fatty acid β-oxidation have not yet been identified. EcoCyc reaction equation: ETF-Reduced + ETR-Quinones -> ETF-Oxidized + ETR-Quinols + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT...

## Biological Role

Products: H+ (molecule.C00080).

## Annotation

ETF:quinone oxidoreductases (ETF-QO) are membrane-associated proteins that accept electrons from electron-transfer flavoprotein at their iron-sulfur site and transfer them to quinone at their flavin-binding site . The first purified ETF-QO was obtained from beef heart mitochondria . The best characterized enzymes are those from human , pig liver , and the metabolically complex photosynthetic purple bacterium Rhodobacter sphaeroides, whose ETF-QO shows high homology to the human ETFDH . Mutations in ETF and ETF-QO that disrupt this reaction activity result in the human inborn error of metabolism disease multiple acyl-CoA dehydrogenation deficiency (MADD) . The electron transfer is actually carried out as two one-electron transfers from ETF FAD semiquinone, instead of one two-electron transfer from a FAD hydroquinone . E. coli contains three ETFab-like gene pairs (ydiQR, ygcQR, and fixAB). FixAB is required for L-carnitine respiration via the CaiA dehydrogenase activity . The ETFs involved in E. coli fatty acid β-oxidation have not yet been identified.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN0-7235`

## Notes

ETF-Reduced + ETR-Quinones -> ETF-Oxidized + ETR-Quinols + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
