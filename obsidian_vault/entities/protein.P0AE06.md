---
entity_id: "protein.P0AE06"
entity_type: "protein"
name: "acrA"
source_database: "UniProt"
source_id: "P0AE06"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303, ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137}. Note=An unlipidated version of this protein (directed to the periplasm by the OmpA signal sequence) functions normally. {ECO:0000269|PubMed:9878415}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acrA lir mtcA b0463 JW0452"
---

# acrA

`protein.P0AE06`

## Static

- Type: `protein`
- Source: `UniProt:P0AE06`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303, ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:16079137}. Note=An unlipidated version of this protein (directed to the periplasm by the OmpA signal sequence) functions normally. {ECO:0000269|PubMed:9878415}.

## Enriched Summary

FUNCTION: Periplasmic adaptor component of the AcrAB-TolC efflux system that confers multidrug resistance (PubMed:9878415). The AcrAB-TolC efflux system has a broad substrate specificity, acting as a substrate:proton antiporter, using proton motive force to export substrates (Probable). AcrA is elongated in shape, being long enough to span the periplasm, linking AcrB and TolC stably together, perhaps promoted by binding to peptidoglycan (PubMed:22308040, PubMed:9878415). AcrA is also a component of the AcrABZ-TolC efflux system, where the small accessory protein AcrZ, together with membrane lipids, may influence the specificity of drug export (PubMed:23010927, PubMed:28355133). {ECO:0000269|PubMed:22308040, ECO:0000269|PubMed:23010927, ECO:0000269|PubMed:28355133, ECO:0000269|PubMed:9878415, ECO:0000305|PubMed:28355133}. AcrA is the periplasmic lipoprotein component of the AcrAB-TolC and AcrAD-TolC multidrug efflux pumps. An acrA IS2 insertion mutant (strain N43) has increased susceptibility to acriflavine, mitomycin C, erythromycin, fusidic acid, novobiocin and ethidium bromide; acrA encodes a predicted lipoprotein; the major portion of the protein is located in the periplasm . The AcrA signal sequence is cleaved upon maturation; Cys25 is required for cleavage . An AcrA derivative, lacking the signal peptide and lipid modification site is functional for drug efflux...

## Biological Role

Component of multidrug efflux pump AcrAD-TolC (complex.ecocyc.CPLX0-3932), multidrug efflux pump AcrAB-TolC (complex.ecocyc.TRANS-CPLX-201).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Periplasmic adaptor component of the AcrAB-TolC efflux system that confers multidrug resistance (PubMed:9878415). The AcrAB-TolC efflux system has a broad substrate specificity, acting as a substrate:proton antiporter, using proton motive force to export substrates (Probable). AcrA is elongated in shape, being long enough to span the periplasm, linking AcrB and TolC stably together, perhaps promoted by binding to peptidoglycan (PubMed:22308040, PubMed:9878415). AcrA is also a component of the AcrABZ-TolC efflux system, where the small accessory protein AcrZ, together with membrane lipids, may influence the specificity of drug export (PubMed:23010927, PubMed:28355133). {ECO:0000269|PubMed:22308040, ECO:0000269|PubMed:23010927, ECO:0000269|PubMed:28355133, ECO:0000269|PubMed:9878415, ECO:0000305|PubMed:28355133}.

## Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3932|complex.ecocyc.CPLX0-3932]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6 | EcoCyc transporter component coefficient=6
- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6 | EcoCyc transporter component coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0463|gene.b0463]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE06`
- `KEGG:ecj:JW0452;eco:b0463;ecoc:C3026_02270;`
- `GeneID:75170481;75202888;945112;`
- `GO:GO:0005886; GO:0009410; GO:0009636; GO:0015125; GO:0015567; GO:0015721; GO:0015895; GO:0015908; GO:0030288; GO:0042802; GO:0042908; GO:0046677; GO:0098567; GO:0140330; GO:1990281`

## Notes

Multidrug efflux pump subunit AcrA (AcrAB-TolC multidrug efflux pump subunit AcrA) (Acridine resistance protein A) (Membrane fusion protein AcrA)
